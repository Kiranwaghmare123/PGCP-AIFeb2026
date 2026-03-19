try:
    with open("abc111.txt","r") as f :
        print(f.read())
except FileNotFoundError:
    print("Nahi hai !")
    