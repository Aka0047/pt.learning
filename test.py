a = "Hello, World!"
print(len(a))
txt ="Ich mag schkolode"
print("Ich"in txt)

txt = "Ich hasse schkolode"
if "hasse" in txt:
    print("yes")

    q= "arda"
    print(q[2:5])

    a = "Hello, World!"
print(a.upper())

a="Arda"
b="İdil"
c= a+" "+b
#boşluk bırakmak istersen
print(c)



#önemli
age= 18
txt= "I am John and {}"
print(txt.format(age))




a=35
b=48

if a>b:
    print("a is greater than b")
else:
    print("b is greater than a")





def myFunction() :
    return True
#anlamadım

print(myFunction())


def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!") #anlamadım



x = 0.2
print(isinstance(x, float))


thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
print(len(thislist))


list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)





mylist = ["apple", "banana", "cherry"]
print("type: "+ str(type(mylist)))   #anlamadım




thislist = ["volvo","audi" ,"mercedes", "porsche", "skoda"]
print(thislist[-3:-1])

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")



  thislist = ["arda", "ahmet", "mehmet"]
  thislist[2]= "Yaşar"
  print(thislist)


thislist = ["arda", "ahmet", "mehmet"]
thislist[1:2] = ["Deniz", "Yaşar"]
print(thislist)

thislist = ["orange", "banana", "cherry"]
thislist.append("volvo")
print(thislist)


thislist = ["orange","apple","banane"]
thislist.insert(1,"range")
print(thislist)

thislist= ["volvo","audi","mercedes"]
hybrid =["toyota","skoda"]
hybrid.extend(thislist)
print(hybrid)

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

  thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])



cars = ["volvo", "porsche", "bmw","volkswagen"]
newlist = []
for x in cars:
   if "v" in x:
    newlist.append(x)

print(newlist)


thislist = ["auto", "ship"]
for x in thislist:
   print(x)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

thislist.sort()

print(thislist)
#büyük harfliler önde geliyor

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

thislist.sort(reverse = True)

print(thislist)


def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
#ilginç
thislist.sort(key = myfunc)

print(thislist)


x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

fruits = ("apple", "banana", "cherry")

(green, yellow, blue) = fruits

print(green)
print(yellow)
print(blue)



thislist= ["a","b","c"]
thislist.append("d")
print(thislist)


a = 400
b = 201
c = 500
if a > b and c > a:
  print("Both conditions are True")
if a>b and a>c:
  print("you doin great")

  
  
  
  
  
  
x=41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

i = 1
while i < 6:
  print(i)
  i += 1

thisdict ={
  "brand": "ford",
  "model":"Mustang",
  "year":1964
  }
print(thisdict["brand"])

thisdict = dict(name = "John", age = 36, country = "Norway")

print(thisdict) 

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

