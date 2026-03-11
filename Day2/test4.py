day = -3
match day:
    case 1:
        print("Monday")
    case "b" | "d":
        print("Tuesday")
    case "c":
        print("Wednesday 1")
    case 'c':
        print("Wednesday 2")
    case "Mumbai"| "Goa":
        print("Wednesday 3")
    case n if n>0:
        print("Wednesday 4")
    case _:
        print("No day")
print("Break is over.................. !")