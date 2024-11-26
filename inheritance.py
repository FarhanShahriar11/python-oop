class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        return "Animal sound"



class Dog(Animal):
    def __init__(self, name, breed):
        
        super().__init__(name, "Dog")  
        self.breed = breed

    # Overriding the 'speak' method from the parent class
    def speak(self):
        
        animal_sound = super().speak()  # Calls the speak method from Animal class

       
        print(f"Name: {self.name}, Species: {self.species}")
        print(animal_sound, "and", self.name, "barks!")



dog = Dog("Buddy", "Golden Retriever")


dog.speak()