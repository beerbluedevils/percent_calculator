import os


def find_value_of_percentage():
    print("\nWhat is the value of this percentage?")
    percent = int(input("Enter The Percentage : "))
    number = int(input("Enter The Value : "))
    result = (percent / 100) * number
    round_result = "{:.1f}".format(result)
    print(f'{percent}% Of The Value {number} is {round_result}')
    input("\nPress Enter To Continue...")
    os.system('cls||clear')
    

def find_percentage_of_value():
    print("\nWhat is the percentage of this value?")
    value_amount = int(input("Enter The Amount Of Value : "))
    total_amount = int(input("Enter The Total Amount : "))
    result = (value_amount / total_amount) * 100
    round_result = "{:.1f}".format(result)
    print(f'The Amount Of {value_amount} is {round_result}% Of {total_amount}')
    input("\nPress Enter To Continue...")
    os.system('cls||clear')

while True:
  try:
    print("This is the Percentage Calculator \nPlease Select The Option")
    print("A. Find the value from percentage \nB. Find the percentage from total value")
    option = input("\nYour option is : ")
    if option == "A":
        find_value_of_percentage()
    elif option == "B":
        find_percentage_of_value()
    else:
        print("Please Choose The Valid Option!\n")
    continue
  except ValueError:
    print("\nPlease Enter The Number!!\n")

