# Import MongoClient from pymongo to connect to the MongoDB server
from pymongo import MongoClient

# Import helper functions from other Python modules
# list_all: function that lists all documents in a Mongo collection
# insert_school: function that inserts a new document into a Mongo collection
# top_students: function you’ll create to return students sorted by average score
list_all = __import__('8-all').list_all
insert_school = __import__('9-insert_school').insert_school
top_students = __import__('101-students').top_students


# Run only if this script is executed directly (not imported)
if __name__ == "__main__":

    # Create a MongoDB client instance that connects to the local MongoDB server
    client = MongoClient('mongodb://127.0.0.1:27017')

    # Access the database `my_db` and the collection `students`
    students_collection = client.my_db.students

    # Define a list of students, each student has a name and a list of topics with scores
    j_students = [
        {
            'name': "John",
            'topics': [
                {'title': "Algo", 'score': 10.3},
                {'title': "C", 'score': 6.2},
                {'title': "Python", 'score': 12.1}
            ]
        },
        {
            'name': "Bob",
            'topics': [
                {'title': "Algo", 'score': 5.4},
                {'title': "C", 'score': 4.9},
                {'title': "Python", 'score': 7.9}
            ]
        },
        {
            'name': "Sonia",
            'topics': [
                {'title': "Algo", 'score': 14.8},
                {'title': "C", 'score': 8.8},
                {'title': "Python", 'score': 15.7}
            ]
        },
        {
            'name': "Amy",
            'topics': [
                {'title': "Algo", 'score': 9.1},
                {'title': "C", 'score': 14.2},
                {'title': "Python", 'score': 4.8}
            ]
        },
        {
            'name': "Julia",
            'topics': [
                {'title': "Algo", 'score': 10.5},
                {'title': "C", 'score': 10.2},
                {'title': "Python", 'score': 10.1}
            ]
        }
    ]

    # Insert each student document into the MongoDB collection using insert_school()
    for j_student in j_students:
        insert_school(students_collection, **j_student)

    # Retrieve all documents (students) in the collection
    students = list_all(students_collection)

    # Print all student documents before computing averages
    for student in students:
        print("[{}] {} - {}".format(
            student.get('_id'),           # the document’s unique ID
            student.get('name'),          # student’s name
            student.get('topics')         # list of topics and their scores
        ))

    # Call the top_students() function to get students sorted by their average score
    top_students = top_students(students_collection)

    # Print each student’s name and their computed averageScore
    for student in top_students:
        print("[{}] {} => {}".format(
            student.get('_id'),           # document ID
            student.get('name'),          # student name
            student.get('averageScore')   # computed average score from topics
        ))

