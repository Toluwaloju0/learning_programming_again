#!/usr/bin/python3
""" a script to get the scores of students in ordered format"""

def top_students(mongo_collection):
    """ a function to get the scores of students in a script"""

    return list(mongo_collection.aggregate([
        {
            # Add a new field 'averageScore' that is the average of all topic scores
            "$addFields": {
                "averageScore": { "$avg": "$topics.score" }
            }
        },
        {
            # Sort students by their averageScore in descending order
            "$sort": { "averageScore": -1 }
        }
    ]))