#Working on calculatoe
operator_sig= input("Enter the operation (+, -, *, /, //): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: ")) 

if operator_sig == "+":
    result = num1 + num2 
elif operator_sig == "-":
    result = num1 - num2 
elif operator_sig == "*":
    result = num1 * num2 
elif operator_sig == "/":
           result = num1 / num2
elif operator_sig == "//":
    result = num1 // num2
else:
    result = "Invalid operation"   
print("The result is", result)    #Print the result

