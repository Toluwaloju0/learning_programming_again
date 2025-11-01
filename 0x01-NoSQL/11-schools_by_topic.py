#!/usr/bin/python3
""" a script to find documents containing a topic"""

def schools_by_topic(mongo_collection, topic):
    """ a function to get all documents containing a topic"""

    return mongo_collection.find({"topics": topic})