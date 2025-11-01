#!/usr/bin/env python3
""" a script to update a document in a colloection"""

def update_topics(mongo_collection, name, topics):
    """ a functio n to update the topic a document"""

    mongo_collection.update_one({"name": name}, {"$set": {"topics": topics}})