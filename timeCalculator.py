import timeCalculatorDependencies

end = False

while True:
    if end == True:
        break

    while True:
        try:
            option = input(""" Options:
            Add 2 times: A
            Find difference between two times: B
            Convert to Hours: C
            Convert to Minutes: D
            Convert Minutes to UTC: E
            Convert Hours to UTC: F
            Convert Days to UTC: G
            EXIT: H
            """).lower()
        except ValueError:
            print("Invalid Value")
            continue
        match option:
            case "a": #i refuse to add this, effort
                print("saw this afterwards, I refuse :)")
                break
            case "b": #works
                time = input("please enter the first date in order dd:hh:mm")
                split1 = time.split(":")
                time2 = input("please enter a second time in the same format")
                split2 = time2.split(":")
                timeCalculatorDependencies.timeDifference(split1, split2)
                break
            case "c": #works
                 time = input("please enter the first date in order dd:hh:mm")
                 split1 = time.split(":")
                 timeCalculatorDependencies.convertHours(split1)
                 break
            case "d": #works
                time = input("please enter the first date in order dd:hh:mm")
                split1 = time.split(":")
                print(timeCalculatorDependencies.convertMinutes(split1))
                break
            case "e": #convert minute to time UTC
                minutes = float(input("please enter time in minutes"))
                print(timeCalculatorDependencies.convertTime(minutes, 3))
                break
            case "f": #convert hours to time UTC
                hours = float(input("please enter time in hours"))
                print(timeCalculatorDependencies.convertTime(hours, 2))
                break
            case "g": #convert days to time UTC
                minutes = float(input("please enter time in days"))
                print(timeCalculatorDependencies.convertTime(minutes, 1))
                break
            case "h": #kill
                end = True
                break
            

        
        




