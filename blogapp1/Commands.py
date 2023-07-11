# # a मा जे जे छ, त्यो Display गर्न परे मा :
# for i in a:
#     print(i.id, i.name, i.email, i.address, i.message)

# # SELECT * FROM Contact
  # a = Contact.objects.all()

# # INSERT INTO Contact VALUES ("Ram", "ram.ram@ram.ram", "myHome", "myMessage")
  # # Method 1
  # a = Contact(name="Ram",email="ram.ram@ram.ram", address="myHome", message="myMessage")
  # a.save()
  # # Method 2
  # Contact.objects.create(name="Ram", email="ram.ram@ram.ram", address="myHome",message="myMessage")

# # SELECT * FROM Contact WHERE name = "Ram"
  # a = Contact.objects.filter(name="Ram")

# # DELETE FROM Contact WHERE id=7
  # Contact.objects.filter(id=3).delete()

# # UPDATE TABLE Contact SET name="Ram Hari" WHERE id=3
  # a = Contact.objects.filter(id=3).update(name="Ram Hari")

# # SELECT * FROM Contact WHERE address LIKE "%Kathmandu%"
  # a = Contact.objects.filter(address__icontains="Kathmandu")

# # SELECT * FROM Contact WHERE address LIKE "Kathmandu%"
  # a = Contact.objects.filter(address__startswith="Kathmandu")

# # SELECT * FROM Contact WHERE address LIKE "%Kathmandu"
  # a = Contact.objects.filter(address__endswith="Kathmandu")

# a = Contact.objects.order_by('name')
# a = Contact.objects.order_by('-name')

# # SELECT * FROM Contact WHERE id IN (3, 4, 5, 6)
  # a = Contact.objects.filter(id__in=[3,4,5,6]) 

# # SELECT * FROM Contact WHERE name LIKE "s%" AND address="myHome"
  # a = Contact.objects.filter(name__startswith="s", address="myHome")

# # SELECT * FROM Contact WHERE Address LIKE "Kathmandu%" OR Address = "Laliptur"
  # from django.db.models import Q
  # a = Contact.objects.filter(Q(name__startswith="s") | Q(address="D"))