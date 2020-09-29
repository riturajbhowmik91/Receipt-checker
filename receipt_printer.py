print("\t\t\twelcome Neramoy Medicals \t\n")
try:
    name = input("Enter Coustomer Name\n").upper()
    Drname= input("Enter Doctor Name\n").upper()
    dict = {}
    sum = 0
    while True:

        lst_of_items = input("Enter The Medicine Name  or 'Enter 'Q' for quit items'\n").capitalize()

        if lst_of_items == "Q":

            for key, value in dict.items():

                print("\n","Medicine Name", key,"Amount", value)

            print(f'\n{name} Bill total is {sum}. Thanks for shopping with us')
            break

        value_of_items = eval(input("Enter The Amount\n"))

        dict.update({lst_of_items: value_of_items})

        sum = sum + float(value_of_items)

        print(f"\nYour Total so far {sum} \n")



except Exception as e:
    print("\nWRONG INPUT!!!")
