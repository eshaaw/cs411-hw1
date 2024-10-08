from typing import Optional

from wildlife_tracker.animal_managment.animal import Animal

class AnimalManager:

    def __init__(self) -> None:
        animals: dict[int, Animal] = {}
        aCounter = 0

    def get_animal_by_id(self, animal_id: int) -> Optional[Animal]:
        if animal_id in self.animals:
            return self.animals[animal_id]
        return None
       

    def register_animal(self, Animal) -> None:
        self.animals[self.aCounter] = Animal
        self.aCounter += 1
        

    def remove_animal(self, animal_id: int) -> None:
        if animal_id in self.animals:
            del self.animals[animal_id]
    
