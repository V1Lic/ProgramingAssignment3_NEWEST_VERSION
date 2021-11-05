#Veljko Ilic
#Programing Assignment #3 NEWEST VERSION

#Quidditch Score Total def

def quidditch_score_total():
    goals = int(input("Enter how many goals were scored in this game:"))
    while goals <0:
        print("ERROR")
        goals = int(input("Enter how many goals were scored in this game:"))
    result = goals * 10
    snitch = str(input("Enter yes if snitch was caught in this game:"))
    snitch == "yes"
    snitch = snitch.lower()
    if snitch == "yes":
        result = result + 30
        print(result)
    else:
        return print(result)

#Quarterback Rating def
def quarterback_rating():
    attempts = int(input("Enter number of passes quarterback attempted:"))
    while attempts <0:
        print("ERROR")
        attempts = int(input("Enter number of passes quarterback attempted:"))
    completions = int(input("Enter number of completion passes:"))
    while completions <0:
        print("ERROR")
        completions = int(input("Enter number of completion passes:"))
    touchdown_passes = int(input("Enter number of touchdown passes:"))
    while touchdown_passes <0:
        print("ERROR")
        touchdown_passes = int(input("Enter number of touchdown passes:"))
    interceptions = int(input("Enter number of interceptions:"))
    while interceptions <0:
        print("ERROR")
        interceptions = int(input("Enter number of interceptions:"))
    passing_yards = int(input("Enter the number of passing yards of quarterback:"))
    while passing_yards <0:
        print("ERROR")
        passing_yards = int(input("Enter the number of passing yards of quarterback:"))
    perfect_passer = 100 * (5*(completions/attempts - 0.3) + 0.25*(passing_yards/attempts-3) + 20*(touchdown_passes/attempts) + 2.375 - (25 * interceptions/attempts))/6
    print("Quarterback score is:", perfect_passer)
    if perfect_passer >= 158.3:
        print("Quarterback is a perfect passer")
    else:
        print("Quarterback is not a perfect passer")

#Gymnast Score def
def gymnast_score():
    difficulty = int(input("Enter number for difficulty(number from 0-10):"))
    while difficulty <0 or difficulty >10:
        print("You need to enter number from 0-10")
        difficulty = int(input("Enter number for difficulty(number from 0-10):"))
    execution1 = int(input("Enter first execution score(number from 0-10):"))
    while execution1 <0 or execution1 >10:
        print("You need to enter number from 0-10")
        execution1 = int(input("Enter first execution score(number from 0-10):"))
    execution2 = int(input("Enter second execution score(number from 0-10):"))
    while execution2 <0 or execution2 >10:
        print("You need to enter number from 0-10")
        execution2 = int(input("Enter second execution score(number from 0-10):"))
    execution3 = int(input("Enter third execution score(number from 0-10):"))
    while execution3 <0 or execution3 >10:
        print("You need to enter number from 0-10")
        execution3 = int(input("Enter third execution score(number from 0-10):"))
    execution4 = int(input("Enter forth execution score(number from 0-10):"))
    while execution4 <0 or execution4 >10:
        print("You need to enter number from 0-10")
        execution4 = int(input("Enter forth execution score(number from 0-10):"))
    execution5= int(input("Enter fifth execution score(number from 0-10):"))
    while execution5 <0 or execution5 >10:
        print("You need to enter number from 0-10")
        execution5 = int(input("Enter fifth execution score(number from 0-10):"))
    hightest = max(execution1, execution2, execution3, execution4, execution5)
    lowest = min(execution1, execution2, execution3, execution4, execution5)
    drop_score = hightest + lowest
    final_score = difficulty + (execution1 + execution2 + execution3 + execution4 + execution5 - drop_score)/3
    print("Final score of this game is:", final_score)

def game_menu():
    print("\t CHOOSE ONE OF 4 OPTIONS:\n"
          "\t 1.Quidditch Game\n"
          "\t 2.Rate your quarterback \n"
          "\t 3.Gymnastic game \n"
          "\t 4.Exit \n")
    option = int(input("Enter your option (1-4):"))
    while option <=0 or option >4:
        print("ERROR")
        option = int(input("Enter your option (1-4):"))
    if option == 1:
        quidditch_score_total()
    elif option == 2:
        quarterback_rating()
    elif option == 3:
        gymnast_score()
    elif option == 4:
        print("See you again")

game_menu()