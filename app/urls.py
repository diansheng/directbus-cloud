from django.conf.urls import url

urlpatterns = [
#     url(r'^train/(?P<count>[0-9]+)/$', training, name='train'),
#     url(r'^instruction/$', instruction, name='instruction'),
#     url(r'^submit/$', submit, name='submit'),
]

from django.contrib.auth import views as auth_views

urlpatterns += [
    url(r'^login/$', auth_views.login, {'template_name':'app/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page':'login'}, name='logout'),
]