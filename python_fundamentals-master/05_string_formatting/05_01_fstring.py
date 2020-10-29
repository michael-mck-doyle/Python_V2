'''
Using f-strings, print out the name, last name, and quote of each person in the given dictionary,
formatted like so:

"The inspiring quote" - Lastname, Firstname

'''

famous_quotes = [
    {"full_name": "Isaac Asimov", "quote": "I do not fear computers. I fear lack of them."},
    {"full_name": "Emo Philips", "quote": "A computer once beat me at chess, but it was no match for me at "
                                          "kick boxing."},
    {"full_name": "Edsger W. Dijkstra", "quote": "Computer Science is no more about computers than astronomy "
                                                 "is about telescopes."},
    {"full_name": "Bill Gates", "quote": "The computer was born to solve problems that did not exist before."},
    {"full_name": "Norman Augustine", "quote": "Software is like entropy: It is difficult to grasp, weighs nothing, "
                                               "and obeys the Second Law of Thermodynamics; i.e., it always increases."},
    {"full_name": "Nathan Myhrvold", "quote": "Software is a gas; it expands to fill its container."},
    {"full_name": "Alan Bennett", "quote": "Standards are always out of date.  That’s what makes them standards."}
]

print("1. Using 'For loop' and list and dictionary methods")
print()
for author_quote in famous_quotes:  # iterates through each item in a list
    author_name = author_quote.get("full_name")  # gets the authors name value as a string from the dictionary
    full_name = author_name.split(" ")  # creates a dictionary containing first and last names as separate items
    first_name = (full_name[0])  # assigns first item in the list to first_name
    last_name = (full_name[1])  # assigns second item in the list to first_name
    author_quote = author_quote.get("quote")  # gets the quote value as a string from the dictionary
    print(f"\"{author_quote}\" - {last_name}, {first_name}")


def my_name(y):
    author_name = y.get("full_name")  # gets the authors name value as a string from the dictionary
    full_name = author_name.split(" ")  # creates a dictionary containing first and last names as separate items
    first_name = (full_name[0])  # assigns first item in the list to first_name
    last_name = (full_name[1])  # assigns second item in the list to first_name

    return last_name, first_name


print()
print()

print("2. Using a Function for extracting first and last names")
print()
for author_quote in famous_quotes:  # iterates through each item in a list
    x = my_name(author_quote)
    author_quote = author_quote.get("quote")  # gets the quote value as a string from the dictionary

    print(f"\"{author_quote}\" - {x[0]}, {x[1]}")






