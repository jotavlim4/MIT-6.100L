number = int(input("what number to find the cube root of? "))
guess = int(input("what guess to start with? "))

print("the current estimate cubed =", guess**3)

next_guess = guess - ((guess**3 - number)/(3*guess**2))
print("next guess to try =", next_guess)