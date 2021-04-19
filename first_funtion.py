num1 = int(input("Enter number one"))
num2 = int(input("Enter number two"))
num3 = int(input("Enter number three"))
num4 = int(input("Enter number four"))

#Enter the numbers into a list
user_list = [num1, num2, num3, num4]

def user_input_average(user_list):
    #Calculate average and divide by the number of elements in the list(In case it changes in the future)
    overall_average = sum(user_list)/len(user_list)
    #Return average grade to be used later
    return overall_average


print(f"Number average {user_input_average(user_list)}")







    