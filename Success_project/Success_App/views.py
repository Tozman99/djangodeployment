from django.shortcuts import render
from Success_App.models import User
from . import forms 

# Create your views here.

def index(request):
    return render(request,'Success_App/index.html')

def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users':user_list}
    return render(request,'Success_App/users.html',context= user_dict)

def User_form_view(request):
    form = forms.User_form()
    if request.method == 'POST':
        form = forms.User_form(request.POST)
        if form.is_valid():
            print('Complete')
            print('first Name: '+form.cleaned_data['first_name'])
            print('last Name: '+form.cleaned_data['last_name'])
            print('first Name: '+form.cleaned_data['email'])
            form.save(commit=True)
            return index(request)
        else:
            print('Error')
    
    
    return render(request,'Success_App/forms.html',{'form':form})





