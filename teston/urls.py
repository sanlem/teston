from django.conf.urls import include, url
from django.contrib import admin
from pols.views import LogoutView

urlpatterns = [
    # Examples:
    # url(r'^$', 'teston.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls),),
    url(r'^$', 'pols.views.home', name='home'),
    url(r'^register/', 'pols.views.register', name='register'),
    url(r'^logout/', LogoutView.as_view(), name='logout'),
    url(r'^login/', 'pols.views.login_user', name='login'),
    url(r'^account/', 'pols.views.change_data', name='account'),
    url(r'^my_tests/', 'pols.views.my_tests', name='my_tests'),
    url(r'^create/', 'pols.views.create', name='create'),
    url(r'^submit/', 'pols.views.submit', name='submit'),
    url(r'^sollutions/(?P<pwr>.{6})/$', 'pols.views.sollutions', name='sollutions'),
]
