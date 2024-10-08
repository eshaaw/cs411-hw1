from typing import Optional

from wildlife_tracker.migration_tracking.migration import Migration
from wildlife_tracker.migration_tracking.migration_path import MigrationPath

class MigrationPath:

    def __init__(self, migration_path: dict[int, MigrationPath] = {}) -> None: 
        pass


    def get_migration_path_details(self, path_id) -> dict:
        pass

    def update_migration_path_details(self, path_id: int, **kwargs) -> None:
        pass
    