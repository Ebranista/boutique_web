"""
Setting Repository
"""
from typing import Optional
from app.repositories.base import BaseRepository
from app.models.setting import Setting


class SettingRepository(BaseRepository[Setting]):
    """Setting repository with specific operations"""
    
    def __init__(self):
        super().__init__(Setting)
    
    def get_active_settings(self) -> Optional[Setting]:
        """Get active settings (first record)"""
        return self.model.query.first()
