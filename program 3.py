def grade_calculator():
    try:
        grade1 = float(input("Enter first assignement grade between 0-100\n"))
        grade2 = float(input("Enter first assignement grade between 0-100\n"))
        grade3 = float(input("Enter first assignement grade between 0-100\n"))

        #Calculate average grade
        average_mark = (grade1 + grade2 + grade3)/3

        #Check the grades are between 0 and 100
        if average_mark < 0 or average_mark > 100:
            print("Enter a grade between 0-100")
            grade_calculator()
        elif average_mark <= 39:
            print("Grade:", average_mark, "\nYou failed")
        elif average_mark >= 40 and average_mark <= 49:
            print("Grade:", average_mark, "\nYou passed with a Third Class (3rd)")
        elif average_mark >= 50 and average_mark <= 59:
            print("Grade:", average_mark, "\nYou passed with a Lower Second-Class (2:1)")
        elif average_mark >= 60 and average_mark <= 69:
            print("Grade:", average_mark, "\nYou passed with a Upper Second-Class (2:1)")
        elif average_mark >= 70:
            print("Grade:", average_mark, "\nYou passed with a First Class (1st)")

#Error message if the user does not enter a number
    except:
        raise ValueError("You did not enter a valid number")
grade_calculator()
