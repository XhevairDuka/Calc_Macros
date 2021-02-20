
""""
Calculate Macros
Xhevair Duka
Oct 23,2020
This program allows the user to type in their bodyweight and then have the program give them some basic starting macro
nutrient requirements for their specified fitness goal, e.g. losing weight, maintaining, or gaining weight.
Nutrition info to understand. Protein and Carbohydrates are 4 calories. Fat is 9 calories. Protein should typically be
1g per pound of lean body weight.
"""


# Function to calculate shredding or losing weight macros
def shredMacros(bw):

    ShredCals = bw * 13  # Variable to calculate total calories
    ShredProtein = bw  # Variable to calculate total protein
    SProteinCals = ShredProtein * 4  # Variable to calculate total calories of protein
    Fat = 75  # Variable to store total fat
    SFatCals = 75 * 9  # Variable to calculate total calories of fat
    ShredCarbs = (ShredCals - (SProteinCals + SFatCals)) / 4  # Variable for total carbs.

    # Display statements for user
    print("Your Daily Calories are :", ShredCals)
    print("Your Daily Macros are: \nProtein:{}g \nFats:{}g \nCarbs:{}g".format(ShredProtein, Fat, ShredCarbs))


# Function to calculate maintenance calories
def maintainMacros(bw):

    MainCals = bw * 14
    MainProtein = bw
    MProteinCals = MainProtein * 4
    Fat = 75
    MFatCals = 75 * 9
    MainCarbs = (MainCals - (MProteinCals + MFatCals)) / 4

    print("Your Daily Calories are :", MainCals)
    print("Your Daily Macros are: \nProtein:{}g \nFats:{}g \nCarbs:{}g".format(MainProtein, Fat, MainCarbs))


# Function to calculate bulking or gaining weight calories
def bulkMacros(bw):

    BulkCals = bw * 15
    BulkProtein = bw
    BProteinCals = BulkProtein * 4
    Fat = 75
    BFatCals = 75 * 9
    BulkCarbs = (BulkCals - (BProteinCals + BFatCals)) / 4

    print("Your Daily Calories are :", BulkCals)
    print("Your Daily Macros are: \nProtein:{}g \nFats:{}g \nCarbs:{}g".format(BulkProtein, Fat, BulkCarbs))


welcome = "CALCULATE YOUR MACROS"
print(welcome.center(100, "-"))

bodyWeight = int(input("Please enter your current body weight: "))  # Asks user to input body weight for calculations

cont = "y"  # Menu variable to maintain loop

while cont == "y":

    print("\nPlease choose from the options below. \n1: Gain Weight \
          \n2: Maintain \n3: Lose Weight \n4: Exit Program")  # Menu for user

    ask = int(input())  # variable for user choice

    if ask == 1:
        bulkMacros(bodyWeight)  # Function call

    elif ask == 2:
        maintainMacros(bodyWeight)  # Function call

    elif ask == 3:
        shredMacros(bodyWeight)  # Function call

    elif ask == 4:
        print("\nThank you. Exiting the program now.")  # Exits program
        cont = "n"

    else:
        print("\nPlease enter one of the choices given")  # Error message if user doesn't enter correct choice
        continue  # Restart loop



