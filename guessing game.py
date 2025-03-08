secret_number=5
guess_count=0
guess_limit=3
while guess_count < guess_limit:
    guess= int(input("guess the number:"))
    guess_count += 1
    if(guess == secret_number):
        print("u won")
        break
else:
    print("you failed in guess the correct number")