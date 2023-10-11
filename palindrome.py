def is_palindrome(string):
  return string == string[::-1]
string = input("Enter a string: ")
if is_palindrome(string):
  print("smae as when reversed.")
else:
  print("diferent when reveresed")
