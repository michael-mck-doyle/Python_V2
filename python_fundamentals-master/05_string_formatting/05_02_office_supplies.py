'''
Using f-strings, print out the name, last name, and favorite
office supply item of each person in the given dictionary,
formatted like so:

LASTNAME, Name           Office supply item
LONGERLASTNAME, Name     Office supply item

'''

office = [
    {"full_name": "Michael Scott", "item": "world's best boss mug"},
    {"full_name": "Dwight Schrute", "item": "pepper spray"},
    {"full_name": "Jim Halpert", "item": "phone"},
    {"full_name": "Pam Beesly", "item": "post-its"},
    {"full_name": "Ryan Howard", "item": "business cards"},
    {"full_name": "Stanley Hudson", "item": "crossword-puzzle"},
    {"full_name": "Kevin Malone", "item": "m&ms"},
    {"full_name": "Meredith Palmer", "item": "flask"},
    {"full_name": "Angela Martin", "item": "cat food"},
    {"full_name": "Oscar Martinez", "item": "calculator"},
    {"full_name": "Phyllis Lapin", "item": "cut flowers"},
    {"full_name": "Kelly Kapoor", "item": "People magazine"},
    {"full_name": "Toby Flenderson", "item": "files"},
    {"full_name": "Creed Bratton", "item": "mung beans"},
    {"full_name": "Darryl Philbin", "item": "forklift"},
]

print("1. Using 'For loop' and list and dictionary methods")
print()
for office_item in office:  # iterates through each item in a list
    employee_name = office_item.get("full_name")  # gets the authors name value as a string from the dictionary
    full_name = employee_name.split(" ")  # creates a dictionary containing first and last names as separate items
    first_name = (full_name[0])  # assigns first item in the list to first_name
    last_name = (full_name[1])  # assigns second item in the list to first_name
    print(sorted(last_name))
    x = len(last_name)

    office_item = office_item.get("item")  # gets the quote value as a string from the dictionary

    print(f"{last_name}, {first_name} - {office_item}")




