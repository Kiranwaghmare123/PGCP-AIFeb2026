import os

with open("abc.txt","r") as f:
    print(f.tell()) # starting position = 0
    print(f.read(5))
    print(f.tell()) # position after reading 5 characters
    f.seek(0)
    print(f.read())
    
    if os.path.exists("abcabc.txt"):
        print("Yes..........")
    else:
        print("No..........")
    print()
    print(f.name)
    print(f.mode)
    print(f.closed)