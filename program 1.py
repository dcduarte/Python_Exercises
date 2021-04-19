def character():
    
    user_character = input("Insert a character: \n")
    match = "FDN006"

    #Check if the user entered more than 1 character
    if len(user_character)>1:
        print("\nEnter only one character")
        #Ask for a character again
        character()
    elif len(user_character)<1:
        print("\nEmpty string")
        #Ask for a character again
        character()  
    else:
        #Convert the user character to upper case to match original string
        if user_character.upper() in match:
            print("Bingo")
        else:
            print("Afraid not")

character()