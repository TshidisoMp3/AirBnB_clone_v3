#!/usr/bin/python3
"""Test .get() method and .count() methods"""
from models import storage
from models.state import State


print("All objects: {}".format(storage.count()))
print("All State objects: {}".format(storage.count(State)))


first_state_id = list(storage.all(State).values())[0].id
print("First State object: {}".format(storage.get(State, first_state_id)))
print("First State object: {}".format(storage.get(State, "no-id")))
