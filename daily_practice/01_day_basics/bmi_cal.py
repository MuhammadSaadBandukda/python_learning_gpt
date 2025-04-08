def bmi_cal(*,height,weight):
    BMI = weight/height**2
    if BMI < 18.5:
        return f"You are underweight,Your BMI is {BMI}"
    elif BMI < 25:
        return f"You are normal,Your BMI is {BMI}"
    elif BMI < 30:
        return f"You are overweight,Your BMI is {BMI}"
    elif BMI >= 30:
        return f"You are obese,Your BMI is {BMI}"
    
def main():
    height = float(input("Enter your height(metres):"))
    weight = float(input("Enter your weight(kgs):"))
    print(bmi_cal(height=height,weight=weight))


main()


# no comments for this to....