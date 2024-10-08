from typing import Any,List, Optional
from wildlife_tracker.animal_management.animal import Animal

class Animal:

    def __init__(self,
                animal_id: int,
                animals: Optional[List[int]] = None) -> None:
        self.animal_id = animal_id
        # this is Pythonic for
        # if animals is not None:
        #   self.animals = animals
        # else:
        #   self.animals = []
        self.animals = animals or []

    def get_animal_details(self, animal_id) -> dict[str, Any]:
        pass

    def update_animal_details(self, animal_id: int, **kwargs: Any) -> None:
        pass

    pass