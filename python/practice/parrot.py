# Happy Parrot - This parrot is so happy. It accepts a 'thing' as its argument
# and then returns a string where it says how happy it is about the thing!
def happy_parrot(thing):
    print "I am so happy about %s!" %(thing)

 happy_parrot('carrots')
# Boring Parrot - Write a method for a boring parrot that just returns whatever
# string you give him as an argument.
def boring_carrot(thing):
    return thing
boring_carrot('carrots')
# Math Parrot - Create a method that accepts two numbers as arguments and adds
# them together!
def math_carrot (num1, num2):
    return (num1 + num2)
math_carrot(1,2)

# Friendly Parrot - This parrot greets people by returning their name and age
# (don't forget to pass that information in as arguments).

def friendly_parrot (name, age):
    return "Hello " + name + "what's up. You're " + str(age) + "years old"

# Favorites Parrot - Tell this parrot about your three favorite things and he
# will return "I love <that thing> too!" for each of them.
def favorites_parrot(thing1, thing2, thing3):
    return "I love " + str(thing1) +" too!"
    return "I love " + str(thing2) +" too!"
favorites_parrot("apple","banana","carrots")
# Now try calling your methods below with any arguments of your choice and
# print them to the screen. Like this:
print happy_parrot("waffles")
# call your methods here


# Now let's pretend you are a wizard and you want to place a spell on each of
# the parrots so that they speak backwards. How would you do that?




# The spell has been broken and everyone is speaking normally again. The
# parrots are really excited about it though - make them shout in all caps.
def shouting_parrot(parrotfunction):
    x = str(parrotfunction)
    return x.upper
