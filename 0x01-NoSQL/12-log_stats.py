#!/usr/bin/env python3
""" a script to query for nginx logs from a mongo database called nginx"""

from pymongo import MongoClient

nginx = MongoClient('mongodb://127.0.0.1:27017').logs.nginx

print(nginx.count_documents({}), " logs")
print("Methods:")

methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
for method in methods:
    print(f"\tmethod {method}: {nginx.count_documents({'method': method})}")
print(f"{nginx.count_documents({'method': 'GET', 'path': '/status'})} status check")