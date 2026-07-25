"""
Setting Service
"""
from typing import Optional, Dict, Any
from app.repositories.setting_repository import SettingRepository
from app.models.setting import Setting


class SettingService:
    """Setting service with business logic"""
    
    def __init__(self):
        self.setting_repository = SettingRepository()
    
    def get_settings(self) -> Optional[Setting]:
        """Get current settings"""
        return self.setting_repository.get_active_settings()
    
    def update_settings(self, data: Dict[str, Any]) -> Optional[Setting]:
        """
        Update settings
        
        Args:
            data: Settings data to update
            
        Returns:
            Updated settings or None
        """
        settings = self.get_settings()
        
        if not settings:
            # Create initial settings
            settings = self.setting_repository.create(**data)
        else:
            # Update existing settings
            for key, value in data.items():
                if hasattr(settings, key):
                    setattr(settings, key, value)
            
            from app.extensions import db
            db.session.commit()
            db.session.refresh(settings)
        
        return settings
    
    def initialize_default_settings(self) -> Optional[Setting]:
        """Initialize default settings"""
        return self.setting_repository.create(
            shop_name='My Boutique Shop',
            currency='USD',
            currency_symbol='$',
            tax_percentage=18,
            low_stock_limit=10,
            dark_mode=False
        )
