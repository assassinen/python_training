__author__ = 'NovikovII'


from model.contact import Contact

d = {'firstname':"Алексей", 'lastname':"Баранцев"}
print(d)
add_contact = Contact(**d)

print("123")
print(add_contact)