secret_number = 13

guess = int(input("type a guess: "))

if guess == secret_number:
    print("your guess is correct!")
elif guess > secret_number:
    print("too high!")
else:
    print("too low!")




