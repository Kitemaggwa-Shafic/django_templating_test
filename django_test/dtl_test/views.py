from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request, 'index.html')



# user_sign up method to handle the user_signup 
def registration(request):
    # checking is the request is post
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        gender = request.POST['gender']
        age = request.POST['age']
        # created a simple user details list
        user_details = [firstname,lastname,gender,age]
        print(user_details)
        print('Student already registered.')
        return render(
             request, 
             'home.html', 
             {'firstname':firstname, 'lastname':lastname, 'gender':gender, 'age':age})
 
        
 

 
# My default home page
def home(request):
    # return take on arguments, (request, 'page to return', display you need to render with this template)
    return render(request, 'home.html' )