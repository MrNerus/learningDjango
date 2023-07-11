from django.shortcuts import render, redirect
from . models import Contact

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
# Create your views here.
