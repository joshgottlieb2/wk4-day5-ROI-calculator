from glob import glob
from msilib.schema import Class
import json



user_dict = {}
user_list = []
current_user = ''

print("""
==============================
WELCOME TO YOUR ROI CALCULATOR
==============================
""")


class Property:
    def __init__(self, address, initial_investment, extra_expenses, income):
        self.address = address
        self.initial_investment = initial_investment
        self.extra_expenses = extra_expenses
        self.income = income
        return_on_investment = round((int(self.income)/(int(self.initial_investment) + int(self.extra_expenses))) * 100, 2)
        self.ROI = f"{return_on_investment}%"

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = f"{self.first_name} {self.last_name}"
        self.property_list = []
        user_dict[self.user_name] = self
        user_list.append(self.user_name)
    
        # run_logic()

    def add_property(self):
        address = input("Enter the property address: ")
        initial_investment = input("Enter the initial investment: $")
        extra_expenses = input("Enter the extra expenses: $")
        income = input("Enter the income from this property: $")
        new_property = Property(address, initial_investment, extra_expenses, income)
        self.property_list.append(new_property)
        run_logic()

    def remove_property(self):
        print(f"Current Properties:")
        for each in current_user.property_list:
            print(each.address)
        property_to_remove = input("Enter the property you would like to remove: ")
        for idx, each in enumerate(self.property_list):
            if each.address == property_to_remove:
                self.property_list.pop(idx)
        print(f"Updated Properties:")
        for each in current_user.property_list:
            print(each.address)
        run_logic()


def run_logic():
    global current_user
    selection = input("""
What would you like to do?
Enter new user: Press 1
Select User: Press 2
View User's Properties with ROI: Press 3
Add Property: Press 4
Remove a Property: Press 5
Quit: Press 6
Type selection here: """)
    if selection == '1':
        first_name = input("Type in the user's first name: ")
        last_name = input("Type in the user's last name: ")
        current_user = User(first_name, last_name)
        run_logic()

    elif selection == '2':
        for idx, value in enumerate(user_list):
            print(idx, value)
        current_user = input(f"Select the user name of the user you would like to view: ")
        current_user = user_dict[current_user]
        print(f"""
Current User: {current_user.first_name} {current_user.last_name}
Property List: {current_user.property_list}
""")
        run_logic()

    elif selection == '3':
        print(f"""
Current User: {current_user.first_name} {current_user.last_name}
Property List:
""")
        for each in current_user.property_list:
            print(each.address, each.ROI)
        # print(user_dict)
        run_logic()
    elif selection == '4':
        current_user.add_property()
            
    elif selection == '5':
        current_user.remove_property()
   

    elif selection == '6':
        quit()
        

if __name__ == '__main__':
    run_logic()