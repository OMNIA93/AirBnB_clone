#!/usr/bin/python3
"""Define base_model class"""

import uuid
from datetime import datetime
from models.engine import storage

class BaseModel:
    """Defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initialize a new instance of BaseModel"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            self._create_instance_from_dict(*args, **kwargs)

    def _create_instance_from_dict(self, *_args, **kwargs):
        """Create a new instance from dictionary input"""
        for k, value in kwargs.items():
            if k in ["updated_at", "created_at"]:
                time_format = "%Y-%m-%dT%H:%M:%S.%f"
                time = datetime.strptime(value, time_format)
                setattr(self, k, time)
            elif k != "__class__":
                setattr(self, k, value)

    def __str__(self):
        """Return a string representation of the instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict())

    def save(self):
        """Update the updated_at attribute with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return a dictionary representation of the instance"""
        result = self.__dict__.copy()
        result["__class__"] = self.__class__.__name__
        result["created_at"] = self.created_at.isoformat()
        result["updated_at"] = self.updated_at.isoformat()
        return result

bm = BaseModel()
bm.save()
print(type(bm.updated_at))
d_json = bm.to_dict()
print(type(d_json['updated_at']))
