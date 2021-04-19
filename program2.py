try:
    def grade_calculator():
        assignment_mark = float(input("Enter your mark between 0-100\n"))

        #Check the grades are between 0 and 100
        if assignment_mark < 0 or assignment_mark > 100:
            print("Enter a grade between 0-100")
            grade_calculator()
        elif assignment_mark <= 39:
            print("Grade:", assignment_mark, "\nFail")
        elif assignment_mark >= 40 and assignment_mark <= 49:
            print("Grade:", assignment_mark, "\nThird Class (3rd)")
        elif assignment_mark >=50 and assignment_mark <= 59:
            print("Grade:", assignment_mark, "\nLower Second-Class (2:1)")
        elif assignment_mark >= 60 and assignment_mark <= 69:
            print("Grade:", assignment_mark, "\nUpper Second-Class (2:1)")
        elif assignment_mark >=70:
            print("Grade:", assignment_mark, "\nFirst Class (1st)")

    #Error message if the user does not enter a number
except:
    raise ValueError("You did not enter a valid number")

grade_calculator()
