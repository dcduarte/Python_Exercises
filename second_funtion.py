while True:
    try:
        num1 = int(input("Enter number one: "))
        num2 = int(input("Enter number two: "))
        num3 = int(input("Enter number three: "))
        num4 = int(input("Enter number four: "))
        
        #Enter the numbers into a list
        user_list = [num1, num2, num3, num4]
    
    #If the user did not enter an integer
    except:
        print("You did not enter an integer")

    try:    
        def user_input_average(user_list):
            #Return average grade to be used later
            overall_average = sum(user_list)/len(user_list)
            #Return addition grade to be used later
            return overall_average

        #New function to add all values on the list
        def user_input_addition(user_list):
            #Calculate the sum of all the value of the list
            user_addition = sum(user_list)
            #Return addition grade to be used later
            return user_addition

        print(f"Number average {user_input_average(user_list)}")
        print(f"Number addition {user_input_addition(user_list)}")
        
        #End the while loop and end the program
        break

    #Error message if there is an error in the functions
    except:
        print("There was an error with the functions")








    