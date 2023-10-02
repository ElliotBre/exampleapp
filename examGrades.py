while(True):
    error = False
    try:
        grade = int(input("Enter your grades in numbers: 1-100"))
        level = int(input("Please enter your level 1 or 2"))
    except ValueError:
        print("Please input an int for both.")
        error = True
        continue
    if not error:
        if (grade > 100 or grade < 1) and (level < 1 or level > 2):
            print("Grades must be between 1 and 100.")
            print("Level must be 1 or 2.")
        else:
            break

if(level == 1):
    if grade > 70:
        print("Level 1 Distinction")
    else:
        if grade > 60:
            print("Level 1 Merit")
        else:
            if grade >50:
                print("Level 1 Pass")
            else:
                print("Fail")
else:
    if(level == 2):
        if grade > 65:
            print("Level 2 Distinction")
        else:
            if grade > 50:
                print("Level 2 Merit")
            else:
                if grade > 39:
                    print("level 2 Pass")
                else:
                    print("Fail")
    else:
        print("exception: level is not 1 or 2")
