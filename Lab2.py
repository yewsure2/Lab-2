print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
def display_main_menu():
    print("display_main_menu")
    txt = "welcome to the jungle"

    x = txt.split()

    print(x)

    thislist = ["apple", "banana", "cherry"]
    print(type(thislist))

def calc_average():
    print("calc_average")

def main():
    display_main_menu()
    calc_average()

if __name__ == "__main__":
    main()