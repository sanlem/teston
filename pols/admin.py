from django.contrib import admin
from .models import Poll, Question, Sollution
# Register your models here.

admin.site.register([Poll, Question, Sollution])