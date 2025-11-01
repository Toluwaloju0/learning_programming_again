#!/usr/bin/env python3
""" a script to list all documents in a collection"""

def list_all(mongo_collection):
    """ a function to list all documents in a collection
    Args:
        mongo_collection: a pymongo collection driver connected to mongo database
    Returns: a list of documents in the collection
    """

    return mongo_collection.find()