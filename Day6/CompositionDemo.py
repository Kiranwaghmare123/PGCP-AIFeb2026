class Room:
    def __init__(self, room_type):
        self.room_type = room_type
        
class House:
    def __init__(self):
        self.r1 = Room("Kitchen")
        self.r2 = Room("Balcony")
        
    def display(self):
        print(self.r1.room_type)
        print(self.r2.room_type)
h = House()
h.display()