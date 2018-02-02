from django.conf.urls import url


from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'confrm_email/$', views.confrm_email, name='confrm_email'),

    url(r'index/$', views.index, name='index'),
    url(r'signup_page/$', views.signup_page, name='signup_page'),
    url(r'login_page/$', views.login_page, name='login_page'),
    url(r'logout/$', views.logout, name='logout'),

    url(r'registration/$', views.registration, name='registration'),
    url(r'login/$', views.login, name='login'),
    url(r'verify/$', views.verify, name='verify'),

]
