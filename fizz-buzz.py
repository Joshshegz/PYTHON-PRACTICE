N = int(input("Enter a positive integer: "))
for i in range(1, N):
  if i % 3 == 0: 
    print("Buzz")
  elif i % 5 == 0:
    print("Fizz")
  elif i % 3 == 0 and i % 5 == 0:
    print("FizzBuzz")
  else:
    print(i)
