from typing import Any,List,Optional

from wildlife_tracker.habitat_management.habitat import Habitat
from wildlife_tracker.migration_tracking.migration import Migration
from wildlife_tracker.migration_tracking.migration_path import MigrationPath

class Migration:
     

     def __init__(self,
                species: str,
                current_location: str,
                start_date: str,
                status: str,
                migration_id: int,
                path_id: int,
                migration_path_id: int,
                animals: Optional[List[int]] = None) -> None:
        self.species = species
        self.current_location: current_location
        self.start_date: start_date
        self.status: status
        self.migration_id: migration_id
        self.path_id: path_id
        self.migration_path_id: migration_path_id
        # this is Pythonic for
        # if animals is not None:
        #   self.animals = animals
        # else:
        #   self.animals = []
        self.animals = animals or []

     def get_migration_paths(self) -> list[MigrationPath]:
        pass
     
     def get_migration_paths_by_destination(self, destination: Habitat) -> list[MigrationPath]:
        pass
    
     def get_migration_paths_by_species(self, species: str) -> list[MigrationPath]:
        pass
     
     def get_migration_paths_by_start_location(self, start_location: Habitat) -> list[MigrationPath]:
        pass
     
     
     def get_migrations_by_current_location(self, current_location: str) -> list[Migration]:
        pass
     
     def get_migrations_by_start_date(self, start_date: str) -> list[Migration]:
        pass
     def get_migrations_by_status(self, status: str) -> list[Migration]:
        pass
     

     def get_migration_by_id(self, migration_id: int) -> Migration:
        pass
     
     def get_migration_path_by_id(self, path_id: int) -> MigrationPath:
        pass
     
     def get_migrations_by_migration_path(self, migration_path_id: int) -> list[Migration]:
        pass


     