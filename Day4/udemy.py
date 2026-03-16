class onlineplatform:
    user = 0
    name = " Udemy "
    
    def __init__(self, uname):
        self.name = uname
        onlineplatform.user += 1
        
    @classmethod
    def count(cls):
        print("Count of udemy users:", cls.user)
        
u1 = onlineplatform("Ravi")
u2 = onlineplatform("Neha")
u3 = onlineplatform("Sakshi")
    
onlineplatform.count()