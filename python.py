getal = input("Voer een getal in: ")
getal = int(getal)

if (getal == 0):
    print("Null is niet toegestaan")
elif ((getal % 3 == 0) & (getal % 5 == 0)):
    print("FizzBuzz")
elif (getal % 3 == 0):
    print("Fizz")
elif (getal % 5 == 0):
    print("Buzz")
else:
    print(getal)
