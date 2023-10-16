def my_fun():          #Simple function calling
    print("Hlw my god gifted child")
my_fun()

def name(fname):        #function calling with one argument
    print(fname+"Dolby")
name("Sony ")
name("Boyas ")
name("boat ")
name("Marsell ")

def Fullname(fname,lname):
    print(fname+" "+lname)
Fullname("Rony","dev")
Fullname("manmu","dev")
Fullname("devil","dev")

def my_function(**kid): 
    print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

#Default parameter-----
def defPara(name="Avijit"):
    print("And the winner is " + name)
defPara("Bijay")
defPara("Doulat")
defPara()
defPara("Kivanti")

#passing a list of argument
def myFan(food):
    for x in food:
        print(x)
fruits=["Apple","banana","cherry"]
myFan(fruits)

# having return statement
def funrun(x):
    return 5*x
print(funrun(5))
print(funrun(7))
print(funrun(797))
print(funrun(11))
