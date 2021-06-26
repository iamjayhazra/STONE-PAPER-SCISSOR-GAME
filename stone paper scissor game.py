import random


def gamewin(comp,you):
    if comp == you:
        return None
    elif comp == 's':
        if you == 'p':
            return True
        elif you == 'k':
            return False
    elif comp == 'p':
        if you == 's':
            return False
        elif you == 'k':
            return True
    elif comp == 'k':
        if you == 's':
            return True
        elif you == 'p':
            return False

print("computer Turn: Stone(s) Paper(p) or Knife(k)?")
randno = random.randint(1,3)
if randno == 1:
    comp = 's'
elif randno == 2:
    comp = 'p'
elif randno == 3:
    comp = 'k'

you = input("your Turn: Stone(s) Paper(p) or Knife(k)?")
a = gamewin(comp,you)

print(f"computer choose {comp} ")
print(f"you choose {you} ")

if a == None:
    print("game is a tie")
elif a:
    print("you won")
else:
    print("you lose")
