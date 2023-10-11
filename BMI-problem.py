av_BMI = 60
height = int(input("What is your height"))
weight = int(input("what is your weight?"))

BMI = weight / (height**2)

if BMI - av_BMI < 0:
    print("You are underweight. Consider eating more.")
elif BMI - av_BMI in range(0, 21):
  print("you are overweight")
elif BMI - av_BMI > 21:
    print("you are obese, sllim down a bit")
else:
    print("You have a normal weight,  Keep it up!")