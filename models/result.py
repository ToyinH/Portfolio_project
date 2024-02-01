#!/usr/bin/python
""" holds class result"""
from models.base_model import BaseModel
from datetime import datetime


class Result(BaseModel):
    """Representation of Result """
    election_id = ""
    candidate_id = ""
    vote_count = 0
        
    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)
