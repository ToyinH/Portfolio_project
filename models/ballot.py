#!/usr/bin/python
""" holds class ballot"""
from models.base_model import BaseModel
from datetime import datetime


class Ballot(BaseModel):
    """Representation of ballot """
    election_id = ""
    position = ""
    
    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)
