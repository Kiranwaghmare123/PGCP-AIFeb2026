day = 'd'
match day:
    case "a":
        print("Monday")
    case "b" | "d":
        print("Tuesday")
    case "c":
        print("Wednesday 1")
    case 'c':
        print("Wednesday 2")
    case _:
        print("No day")
print("Break is over.................. !")