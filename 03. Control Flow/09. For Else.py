successful = False

# The else block runs when the for loop finishes normally — without hitting break.
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")
