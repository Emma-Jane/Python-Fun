import sys

#cup to grams converter
#using a dictionary to store keys and values for the ingredient conversion
conversion = {
    "flour": 125,
    "sugar": 200,
    "butter": 227,
    "milk": 244,
    "oil": 218,
    "oats": 90
}

#command-line arguments ingredient and how many cups to convert
ingredient = sys.argv[1]
cups = float(sys.argv[2])

#creating a variable which will find the ingredient argument in the dictionary
#and then times it by the number of cups entered in the argument
grams = conversion[ingredient] * cups

#printing the calcualted result
print("Your ingredient:", ingredient)
print("Cups entered:", cups)
print("Grams needed:", grams)
