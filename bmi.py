print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def calculate_BMI(height, weight):
    print("Height=" + str(height))
    print("Weight=" + str(weight))
    BMI=weight/(height**2)
    print("BMI is" + str(BMI))
    return BMI

def check_BMI(bmi_value):
      if bmi_value < 18.5:
        print("Underweight")
        if bmi_value > 18.5 and bmi_value < 25.0:
            print("normal")
        if bmi_value > 25.0:
            print("overweight")

def classify_weight(weight_classificiation):
    weight_map = {
        "Under weight": -1,
        "Normal weight": 0,
        "Over weight": 1
    }

    return weight_map.get(weight_classificiation, "Invalid weight classification")

def  main():
    bmi_value = calculate_BMI(1.75,80)
    print("calculate bmi value = " + str(bmi_value))

if __name__ == "__main__":
    main()