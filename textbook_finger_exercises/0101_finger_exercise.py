"""
Finger exercise: Write a program that examines three variables—x, y, and z—and
prints the largest odd number among them. If none of them are odd, it should
print a message to that effect.
"""

# solucao

x = 7
y = 10
z = 3



if x % 2 != 0 and (x > y or y % 2 == 0) and (x > z or z % 2 == 0): 
    print(x, "is the largest odd number")    

elif y % 2 != 0 and (y > z or z % 2 == 0): # x é par ou (x <= y e y é par) ou (x <= z e z é par)
    print(y, "is the largest odd number")

elif z % 2 != 0: # y é par ou (y <= z e z é par)
    print(z, "is the largest odd number")

else:
    print("none of them is odd\n")

# para 4 números:

x = 7
y = 10
z = 3
w = 21

if x % 2 != 0 and (x > y or y % 2 == 0) and (x > z or z % 2 == 0) and (x > w or w % 2 == 0):
    print(x, "is the largest odd number") 

elif y % 2 != 0 and (y > z or z % 2 == 0) and (y > w or w % 2 == 0):
    print(y, "is the largest odd number")

elif z % 2 != 0 and (z > w or w % 2 == 0):
    print(z, "is the largest odd number")

elif w % 2 != 0:
    print(w, "is the largest odd number")

else:
    print("none of them is odd")

# solucao mais eficiente sem usar funcoes da linguagem:

x = 7
y = 10
z = 3
w = 21

largest = None

if x % 2 != 0:
    largest = x

if y % 2 != 0 and (y > largest or largest is None):
    largest = y

if z % 2 != 0 and (z > largest or largest is None):
    largest = z

if w % 2 != 0 and (w > largest or largest is None):
    largest = w

if largest is None:
    print("none of them is odd")
else:
    print(largest, "is the largest odd number")
