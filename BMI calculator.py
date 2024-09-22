print("Welcome To Body Mass Index (BMI) calculator")

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in centimeters: "))

height_in_meters = height / 100

BMI = weight / (height_in_meters ** 2)

print("Your Body Mass Index is: ", BMI)

if BMI <= 18.4:
    print("You are underweight")
elif 18.4 < BMI <= 24.9:
    print("Your weight is normal") 
elif 24.9 < BMI <= 29.9:
    print("You are overweight")
else:
    print("You are obese")