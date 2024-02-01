#!/usr/bin/python
""" holds class vote"""
from models.base_model import BaseModel
from datetime import datetime


class Vote(BaseModel):
    """Representation of candidate """
    user_id = ""
    ballot_id = ""
    candidate_id = ""
    
    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)
