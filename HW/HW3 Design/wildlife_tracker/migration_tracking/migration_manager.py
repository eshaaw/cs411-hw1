from typing import Optional,Any, List

from wildlife_tracker.habitat_management.habitat import Habitat
from wildlife_tracker.migration_tracking.migration import Migration
from wildlife_tracker.migration_tracking.migration_path import MigrationPath


class MigrationManager:

    def __init__(self, migration: dict[int,Migration] = {}) -> None: 
        pass

    def get_migrations(self) -> list[Migration]:
        pass

    def cancel_migration(self, migration_id: int) -> None:
        pass

    def get_migration_details(self, migration_id: int) -> dict[str, Any]:
        pass
    
    def update_migration_details(self, migration_id: int, **kwargs: Any) -> None:
        pass

    def schedule_migration(self, migration_path: MigrationPath) -> None:
        pass

    def create_migration_path(self, species: str, start_location: Habitat, destination: Habitat, duration: Optional[int] = None) -> None:
        pass

    def remove_migration_path(self, path_id: int) -> None:
        pass