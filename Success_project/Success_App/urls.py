from django.conf.urls import url 
from Success_App import views 

urlpatterns = [
    url(r'^$',views.users,name='users'),
]