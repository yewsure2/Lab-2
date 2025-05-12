print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def calculate_BMI(height, weight):
    print("Height=" + str(height))
    print("Weight=" + str(weight))
    BMI=weight/(height**2)
    if BMI < 18.5:
        return -1
    elif BMI > 18.5 and BMI < 25.0:
        return 0
    else:
        return 1

def check_BMI(bmi_value):
    if bmi_value < 18.5:
        print("Underweight")
    elif bmi_value > 18.5 and bmi_value < 25.0:
        print("normal")
    else:
        print("overweight")

def main():
    bmi_value = calculate_BMI(1.75,80)
    print("BMI is " + str(bmi_value))
    check_BMI(bmi_value)

if __name__ == "__main__":
    main()