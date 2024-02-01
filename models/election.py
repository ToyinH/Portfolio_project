#!/usr/bin/python
""" holds class election"""
from models.base_model import BaseModel
from datetime import datetime


class Election(BaseModel):
    """Representation of state """
    title = ""
    start_time = ""
    end_time = ""
    is_active = False

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)
