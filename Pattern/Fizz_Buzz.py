#enter a number using custom input
a = int(input("Enter a number: "))
#if the number is divisible by 3 and 5 both return FizzBuzz
if (a%3 == 0 and a%5 == 0):
    print("FizzBuzz")
#if the number is divisible by only 3 return Fizz
elif (a%3 == 0):
    print("Fizz")
#if the number is divisible by only 5 return Buzz
elif (a%5 == 0):
    print("Buzz")
#if not any of them return the number itself
else:
    print(a)

