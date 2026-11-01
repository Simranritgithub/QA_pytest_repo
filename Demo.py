from ctypes import sizeof


print ("hello world")
#Numeric printing
print (1234)
# String printing
print ("This is a string")
#Define variables in one line
a, b, c = 5, 10, "Simran"
print (f"value of a:{a},value of b:{b},value of c:{c}")
print (type(a))
print (type(b))
print (type(c))
# List
my_list = [1, 2, 3, 4, 5,"Simran","4.4",4+5j,(1,2,3),{"name":"Simran","age":22}]
#Integer in list
print (my_list[0])
#String in list
print (my_list[5])
#Float in list
print (my_list[6])
#Complex number in list
print (my_list[7])
#Tuple in list
print (my_list[8])
#Dictionary in list
print (my_list[9])
print (type(my_list))
print (len(my_list))
#Update list
my_list[0] = "RAHUL"
#Delete list
del my_list[1]
print (my_list)
#Length of list after deletion
print (f"Length of list after deletion: {len(my_list)}")
#Dictionary
my_dict = {"name":"Simran","age":22,"city":"Delhi","empty":""}
print (my_dict)
print (type(my_dict))
print(my_dict["name"])
# Adding values to dictionary at runtime
dict={}
dict["name"] = "Simran"
print (dict)
userkey = input("Enter the key : ")
value= input("Enter the value : ")
dict[userkey] = value
print (f"user inputed dictionary: {dict}")
print (type(dict["world"]))
car={"make":"Toyota","model":"Camry","year":2020,"color":"Blue"}
print (f"Car model: {car['model']}")
car["owner"]="Rahul"
print(f"Updated car dictionary: {car}")