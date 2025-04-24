TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

head = """
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Erik Bršlica
email: erik.brslica@gmail.com"""

login_credentials = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123" 
}

separator = "-" * 25

# header
print(head)
print(separator)

# login
user_name = input("username:")
password = input("password:")

print(separator)

if login_credentials.get(user_name) != password:
    print("unregistered user, terminating the program..")
    quit()

# text select intro
texts_count = len(TEXTS)
print("Welcome to the app,", user_name)
print("We have", texts_count, "texts to be analyzed.")
print(separator)

# selecting the text
cislo_textu = input("Enter a number btw. 1 to " + str(texts_count) + " to select: ")
range_textu = list(range(1, texts_count + 1))

if not cislo_textu.isnumeric():
    print("Invalid data type")
    quit()
if not int(cislo_textu) in range_textu:
    print("Selected number not in range")
    quit()
print(separator)