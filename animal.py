class Animal:
    def __init__(self, name, group, number_of_legs, skills):
        self.name = name
        self.group = group
        self.number_of_legs = number_of_legs
        self.skills = skills

    def show_info(self):
        return (f"Name: {self.name}\n"
                f"Group: {self.group}\n"
                f"Number of Legs: {self.number_of_legs}\n"
                f"Skills: {self.skills}\n")


tiger = Animal("Tiger", "Feline", 4, ["Running fast", "Swimming", "Strong Chin", "Strong claw"])
snake = Animal("Snake", "Reptile", 0, ["Make rapid progress", "Strong bite", "Strong claw"])
frog = Animal("Frog", "Amphibians", 4, ["Jumping high", "Swimming", "Deadly Poison"])
boar = Animal("Wild Boar", "Suidae", 4, ["80 KM per hour", "Long and sharp teeth", "Strong sense of smell"])
bear = Animal("Polar Bear", "Ursidae", 4, ["Wonderful speaking with humans", "Fishing", "Destroy beehive"])


print(bear.show_info())
print(boar.show_info())
print(frog.show_info())
print(tiger.show_info())
print(snake.show_info())


dictiger = {
"Name" : "Tiger",
"Group" : "Feline",
"Number of Legs" : 4,
"Skills" : "Running fast , Swimming , Strong Chin , Strong claw"
}
dictsnake ={
"Name" : "Snake",
"Group" : "Reptile",
"Number of Legs" : 0,
"Skills" : "Make rapid progress , Strong bite , Strog claw"
}
dictfrog = {
"Name" : "Frog",
"Group" : "Amphibians",
"Number of Legs" : 4,
"Skills" : "Jumping high , Swimming , Deadful Posion"
}
dictboar = {
"Name" : "Wild Boar",
"Group" : "Suidae",
"Number of Legs" : 4,
"Skills" : "80 KM per hour , Long and sharp teeth , Strong sense of smell"
}
dictbear = {
"Name" : "Polar Bear",
"Group" : "Ursidae",
"Number of Legs" : 4,
"Skills" : "Wonderful speaking with humans , Fishing , Destroy beehive"
}


















print("This project Made by Tuna Basar KASAP")
