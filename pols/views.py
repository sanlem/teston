from django.shortcuts import render, render_to_response
from django.views.generic.base import View
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from .models import Poll, Question, Sollution
from random import choice


def home(request):
	return render(request, "index.html", {"user": request.user})

def register(request):
    """if request.method == "GET":
        data, errors = {}, {}"""
    if (request.method == "POST") and request.user.is_anonymous():
        if request.POST.get("register_button") is not None:
            data = {'username': request.POST.get('username'),
                'pwr1': request.POST.get('pwr1'),
                'pwr2': request.POST.get('pwr2')}
            errors = {}
            username = request.POST.get('username', ' ').strip()
            if not username:
                errors["username"] = "Enter a login"
            else:
                data["username"] = username
            
            """if len(User.objects.filter(username=username)) != 1:
                errors["username"] = "Such user already exists"
            """

            try:
                User.objects.get(username = data['username'])
            except User.DoesNotExist:
                pass
            else:
                errors["username"] = "Such user already exists"

            pwr1 = request.POST.get("pwr1")

            if " " in pwr1:
                errors["pwr1"] = "Invalid password"

            pwr2 = request.POST.get("pwr2")
            
            if len(pwr1) < 6:
                errors["pwr1"] = "Too short, at least 6 symbols"
                errors["pwr2"] = ""

            if pwr1 != pwr2:
                errors["pwr1"] = "Passwords don't match"
                errors["pwr2"] = ""

            if not errors:
            	user = User(username=username)
            	user.set_password(pwr1)
            	user.first_name = username
            	user.save()
            	
            	return HttpResponseRedirect(reverse('login'))
            else:
                if request.user.is_anonymous(): 
                    return render(request, "registration/register.html", {'errors': errors, 'data': data})
                else:
                    return HttpResponseRedirect(reverse("home"))

    else:
    	return render(request, "registration/register.html", {})

def login_user(request):
    if request.user.is_anonymous() and request.method == "POST":
        username = request.POST.get("username")
        pwr = request.POST.get("pwr")
        user = authenticate(username=username, password=pwr)
        error = ""
        if user is not None:
            if not user.is_active:
                error = "Account is blocked"
        else:
            error = "Such user doesn't exist"

        if not error:
            login(request, user)
            return HttpResponseRedirect("/")
        else:
            return render(request, "login.html", {'error': error})
    else:
        return render(request, "login.html", {})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")

def change_data(request):
    if request.method == "POST":
        # reset first or last name
        if request.POST.get("changedata_button") is not None:
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            user = User.objects.get(username=request.user.username)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            return HttpResponseRedirect(reverse("account"))
        # reset pwr
        if request.POST.get("changepwr_button") is not None:
            errors = {}
            message = ""
            user = User.objects.get(username=request.user.username)
            username = request.user.username
            if not user.check_password(request.POST.get("old_pwr")):
                errors["old_pwr"] = "Wrong password"
                return render(request, "account.html", {"errors": errors})

            pwr1 = request.POST.get("pwr1")

            if " " in pwr1:
                errors["pwr1"] = "Invalid password"


            pwr2 = request.POST.get("pwr2")
            
            if len(pwr1) < 6:
                errors["pwr1"] = "Too short, at least 6 symbols"
                errors["pwr2"] = ""

            if pwr1 != pwr2:
                errors["pwr1"] = "Passwords don't match"
                errors["pwr2"] = ""

            if not errors:
                user.set_password(pwr1)
                user.save()
                usr = authenticate(username=username, password=pwr1)
                login(request, usr)
                message = "Password changed"
            return render(request, "account.html", {"errors": errors, "message": message})


    elif request.method == "GET":
        if request.user.is_anonymous():
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "account.html", {})

def my_tests(request):
    if request.user.is_authenticated() and request.method == "GET":
        polls = Poll.objects.filter(owner=request.user.username)
        return render(request, "my_tests.html", {"tests": polls})
    else:
        return HttpResponseRedirect(reverse("home"))

def create(request):
    if request.method == "POST":
        data, errors = {}, {}
        title = request.POST.get("title")
        
        questions_amount = int(request.POST.get("questions_amount"))
        if not title:
            errors["title"] = "You should enter a title"
            return render(request, "create.html", {"number": range(1, questions_amount + 1), 
            "answers": range(1, 5), "questions_amount": questions_amount, "errors": errors})
        else:
            data["title"] = title
            description = request.POST.get("description")

            # password generation
            alphabet = list('abcdefghijklmnopqrstuvwxyz' + 'abcdefghijklmnopqrstuvwxyz'.upper())
            pwr = ""
            for i in range(6):
                pwr = pwr + choice(alphabet)
            poll = Poll(title=unicode(title), owner=unicode(request.user.username), questions_number=questions_amount,
                description=unicode(description), password=pwr)
            poll.save()
        # 

        amount = int(request.POST.get("questions_amount"))

        for i in range(1, amount + 1):
            current_question = "question" + str(i)
            question = Question()
            question.title = unicode(request.POST.get(current_question))
            question.poll = poll
            variant = "answer" + str(i) + "_1"
            question.variant_1 = request.POST.get(variant)
            variant = "answer" + str(i) + "_2"
            question.variant_2 = request.POST.get(variant)
            variant = "answer" + str(i) + "_3"
            question.variant_3 = request.POST.get(variant)
            variant = "answer" + str(i) + "_4"
            question.variant_4 = request.POST.get(variant)
            correct = "correct" + str(i)
            question.correct = request.POST.get(correct)
            question.number = int(i)
            question.save()
        return HttpResponseRedirect(reverse("my_tests"))
    else:
        return HttpResponseRedirect(reverse("home"))


def submit(request):
    if request.method == "GET":
    	try:
    	    current_poll = Poll.objects.get(password=request.GET.get("test_pwr"))
    	except Exception:
    	    return HttpResponseRedirect(reverse("home"))
        questions = Question.objects.filter(poll=current_poll)
        return render(request, "test.html", {"questions": questions, "number": range(1, 
            current_poll.questions_number), "poll": current_poll})
    else:
        current_poll = Poll.objects.get(password=request.POST.get("test_pwr"))
        submitter = request.POST.get("submitter")
        group = request.POST.get("group")
        questions_number = current_poll.questions_number
        points = 0
        questions = Question.objects.filter(poll=current_poll)
        for question in questions:
            answer = "answer" + str(question.number)
            if int(request.POST.get(answer)) == question.correct:
                points = points + 1
        sollution = Sollution(poll=current_poll, submitter=submitter, mark=points, group=group)
        sollution.save()

        return HttpResponseRedirect(reverse("home"))

def sollutions(request, pwr):
    poll = Poll.objects.get(password=pwr)
    if poll and poll.owner == request.user.username:
        sollutions = Sollution.objects.filter(poll=poll)
        return render(request, "sollutions.html", {"sollutions": sollutions})
    else:
        return HttpResponseRedirect(reverse("home"))



