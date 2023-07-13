from django.shortcuts import render, redirect
from . models import Contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def Home(request):
    if request.method == "POST":
        Contact.objects.create(
            name=request.POST["name"],
            email=request.POST["email"],
            address=request.POST["address"],
            message=request.POST["message"]
        )
    contacts = Contact.objects.all()
    return render(request,"blogapp1/view.html", {"contacts": contacts})

def Delete(request, id):
    Contact.objects.get(id=id).delete()
    return redirect("home")

def Update(request, id):
    if request.method == "POST":
        Contact.objects.filter(id=id).update(
            name=request.POST["name"],
            email=request.POST["email"],
            address=request.POST["address"],
            message=request.POST["message"]
        )
        return redirect('home')

    myCon = Contact.objects.get(id=id)
    return render(request, "blogapp1/update.html", {"contact":myCon})

def Search(request):
    if request.method == "GET":
        query = request.GET["search"]
        myCon1 = Contact.objects.filter(name__icontains=query)
        myCon2 = Contact.objects.filter(email__icontains=query)
        myCon3 = Contact.objects.filter(address__icontains=query)
        myCon4 = Contact.objects.filter(message__icontains=query)
        myCon = myCon1.union(myCon2,myCon3,myCon4)
        return render(request, "blogapp1/search.html", {"Contacts":myCon})
    
def HandleSignup(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            user = User.objects.create_user(username=username, password=password)
        user.first_name=firstname
        user.last_name=lastname
        user.save()
    return render(request, "blogapp1/signup.html")

def HandleLogin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        print(username, password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect("home")
    return render(request, "blogapp1/login.html")

def HandelLogout(request):
    logout(request)
    return redirect("login")
# Create your views here.
