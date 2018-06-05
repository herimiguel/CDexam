from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from models import *
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def index(request):
    return render(request, 'my_app/index.html')
def register(request):
    if request.method=='POST':
        firstName= request.POST['firstName']
        lastName= request.POST['lastName']
        email= request.POST['email']
        password= request.POST['password']
        isValid=True
        minVal= 3
        maxVP= 8
    if len(request.POST['firstName']) < minVal:
        messages.error(request, 'Name needs to be at least 3 characters!')
        isValid = False
    if len(request.POST['lastName']) < minVal:
        messages.error(request, 'Last Name needs to be at least 3 characters!')
        isValid = False
    if len(request.POST['email']) < minVal:
        messages.error(request, 'Email is required!')
        isValid = False
    if request.POST['email'] != email:
        messages.error(request, 'Email is already registered!')
        isValid = False
    if len(request.POST['password']) < minVal:
        messages.error(request, 'Password is required!')
        isValid = False
    if request.POST['conPassword'] != request.POST['conPassword']:
        messages.error(request, 'Password confirmation failed!')
        isValid = False

    if not isValid:
        return redirect('/')

    if request.POST['conPassword'] == password:
        try:
            user=User.objects.create(firstName=firstName, lastName=lastName, email=email, password=password )
        except IntegrityError:
            messages.error(request, 'This Email is already registered!')
            return redirect('/')
        request.session['user.id']= user.id
    return redirect('my_app:viewItems')        
    # return render(request,'myApp/success.html')

def login(request):
    if request.method=='POST':
        email = request.POST['email']
        password= request.POST['password']
        isValid= True
        minVal= 3
    if len(request.POST['email']) < minVal:
        messages.error(request, 'Email is required!')
        isValid = False
    if len(request.POST['password']) < minVal:
        messages.error(request, 'Password is required!')
        isValid = False
    try:
        User.objects.get(email=request.POST['email'], password= request.POST['password'])
    except ObjectDoesNotExist:
        messages.error(request, "Email and Password don't match!")
        isValid = False
    else:
        messages.error(request, " ")

    if not isValid:
        return redirect('/')
    else:
        request.session['user.id'] = (User.objects.get(email=request.POST['email'])).id
        return redirect('my_app:viewItems') 
        # return render(request, 'my_app/success.html')

# def success(request):
#     if 'user.id' in request.session.keys():
#         user= User.objects.get(id=request.session['user.id'])
#     context={
#         'user': user
#     }
#     return render(request, 'my_app/success.html', context)

def viewItems(request):
    user= request.session['user.id']
    context={
        'items': Item.objects.all().exclude(additions__user_id=user),
        'myItems': Addition.objects.filter(user_id=user),
        'additions': Addition.objects.all(),
        'user': User.objects.get(id=request.session['user.id'])
    }
    return render(request, 'my_app/success.html', context)

def logOut(request):
    request.session.clear()
    messages.success(request, 'Successfully logged out')
    return redirect('/')

def addItem(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.session['user.id'])
        itemName = request.POST['itemName']
        isValid=True
        minVal= 3
        if len(request.POST['itemName']) < minVal:
            messages.error(request, 'COVFEFE! Your Wishlist Item must contian at least 3 characters!')
            isValid = False
        if not isValid:
            return redirect('my_app:viewItems')
        else:
            Item.objects.create(itemName=itemName, creator = user)
            messages.error(request, "HOPE YOUR WISH COMES TRUE")
    return redirect('my_app:viewItems')

def toItems(request, id):
    user= request.session['user.id']
    context={
        'item': Item.objects.get(id=id),
        # 'myItems': Addition.objects.filter(user_id=user),
        'additions': Addition.objects.filter(item_id=id)
    }
    return render(request, 'my_app/show.html', context)

def addToMyItem(request, item_id):
    Addition.objects.create(item_id=item_id, user_id=request.session['user.id'])            
    return redirect('my_app:viewItems')

def deleteItem(request, item_id):
    item= Addition.objects.get(item_id=item_id, user_id=request.session['user.id'])
    item.delete()
    return redirect('my_app:viewItems')

def deleteFromD(request, id):
    item= Item.objects.get(id=id)
    item.delete()
    return redirect('my_app:viewItems')    
