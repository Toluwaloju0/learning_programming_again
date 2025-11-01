#!/usr/bin/env python3
""" a script to insert a document into a monge file"""

def insert_school(mongo_collection, **kwargs):
    """ a function to iinsert a document into monge using a mongo client
    Args:
        mongo_collection: a connection to the mongo collection where the document would be inserted
        kwargs: a dictionary  containing the document
    Returns the _id of the new inserted document
    """

    return mongo_collection.insert_one(kwargs).inserted_id
