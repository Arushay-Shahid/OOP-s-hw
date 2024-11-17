class Robot:
    def __init__(self, name, purpose):
        self.name = name
        self.purpose = purpose

    def introduce(self):
        return f"Hello! I am {self.name}. My purpose is to {self.purpose}."

# Create an instance of the Robot class
my_robot = Robot("Arushay", "I am a student.")

# Call the introduce method
print(my_robot.introduce())
