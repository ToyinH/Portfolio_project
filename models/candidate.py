#!/usr/bin/python
""" holds class candidate"""
from models.base_model import BaseModel
from datetime import datetime


class Candidate(BaseModel):
    """Representation of candidate """
    name = ""
    position = ""
    
    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)
