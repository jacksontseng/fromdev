import random

def walle_talk (talk):
    ran = random.randint(0,100)
    if talk.isupper():
        print str(ran) + "EEEEEEEEEEEVAAAAAAAAAA!"
    else:
        print str(ran) + "Dirrrrr-ect-tivvve?"
# walle_talk("HELLO")
# walle_talk('Hi')
# walle_talk('hi')


def speak_to_walle():
    i = 0
    while i<3:
        hi = raw_input("hello, I'm Walle")
        if hi == "BYE":
            i+=1
        elif not (hi == "BYE") and not i == 0:
         i-=1
        print i
    walle_talk(hi)

speak_to_walle()
