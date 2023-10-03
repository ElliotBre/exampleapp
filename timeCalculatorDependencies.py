def splitTime(split1, split2, num):
    match num:
        case 1:
            new1 = (int(split1[0])) 
            new2 = (int(split2[0])) 
        case 2:
            new1 = (int(split1[1])) 
            new2 = (int(split2[1])) 
        case 3:
            new1 = (int(split1[2])) 
            new2 = (int(split2[2])) 
    splitTimes  = []
    splitTimes.append(new1)
    splitTimes.append(new2)

    return splitTimes

def convertHours(split1):
    total = 0
    print("i am running")
    for i in range(len(split1)):
        new1 = 0
        new1 += int(split1[i])
        match i:
            case 0:
                print("adding days")
                total += (new1 * 24) 
            case 1:
                print("adding hours")
                total += new1 
            case 3:
                print("adding minutes")
                total += new1 * 60
    print(total)
    return total


def convertMinutes(split1):
    total = 0
    for i in range(len(split1)):
        new1 = int(split1[i])
        match i:
            case 0:
                total += ((new1 * 24) * 60) % 1
            case 1: 
                total += (new1 * 60) % 1
            case 2:
                total += new1 % 1

    return total

def convertTime(convert, num):
    utc = []
    match num:
        case 1:
            utc.append(convert % 1)
            convert -= utc[0]
            convert *= 10
            utc.append(convert % 1)
            convert -= utc[1]
            convert *= 10
            utc.append(convert % 1)
        case 2:
            utc.append((convert // 24) % 1)
            convert -= (utc[0] * 24) % 1
            utc.append(convert % 1)
            convert -= utc[1]
            convert *= 10
            utc.append(convert % 1)
        case 3:
            utc.append(((convert // 60) // 24) % 1)
            convert -= ((utc[0] * 24) * 60) % 1
            utc.append(((convert // 60) % 1))
            convert -= (utc[1] * 60) % 1
            utc.append(convert % 1)
    return utc


def difference(splitTimes):
     split1 = splitTimes[0]
     split2 = splitTimes[1]
     if split1 > split2:
        splitDif = split1 - split2
     else:
         splitDif = split2 - split1
     return splitDif

def timeDifference(split1, split2):
    days = splitTime(split1, split2, 1)
    hours = splitTime(split1, split2, 2)
    minutes = splitTime(split1, split2, 3)

    days = difference(days)
    hours = difference(hours)
    minutes = difference(minutes)

    utc = []

    utc.append(days)
    utc.append(hours)
    utc.append(minutes)

    print(f"difference in UTC = {utc}")

    return utc
