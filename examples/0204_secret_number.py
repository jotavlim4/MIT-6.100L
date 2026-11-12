secret_number = 13

guess = int(input("type a guess: "))

if guess == secret_number:
    print(True)
else:
    print(False)

# poderiamos fazer simplesmente:

print(guess == secret_number)