#assignmment-number 2
josh_no = float(input("Enter your number"))

if josh_no%2 == 0:
  print("your number is an even number")
elif josh_no%3 == 0:
  print("your number is an odd number")

def is_prime(n):
  if n <= 1:
    return False

  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False

  return True

josh_no = 11

if is_prime(josh_no):
  print("Number is prime")
else:
  print("Number is not prime")
