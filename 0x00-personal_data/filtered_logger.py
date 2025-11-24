#!/usr/bin/env python3
""" a module to filter the contents of a message by obfuscating some parts"""

import re
import mysql.connector
import os

from typing import List

def filter_datum(
    fields,
    redaction,
    message,
    separator
):
    """ a function to obfuscate a message using regex
    Args:
        field [list]: a list of fields to be obfuscated in the message
        redaction [str]: a string containing what would be used to obscure the message
        message [list of str]: a list containing the messages to be objuscated
        separator [str]: a string containg what seperates arguments in the message
    Return: the list of messages with the parts in fields obscured
    """

    pattern = f"({'|'.join(fields)})=[^{separator}]*"
    replacement = r"\1=" + redaction

    return re.sub(pattern, replacement, message)

import logging

class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)

        self.fields = fields
    
    def format(self, record: logging.LogRecord) -> str:

        return filter_datum(self.fields, self.REDACTION, str(record), self.SEPARATOR)
    

def get_db():
    """ a function to return a connection to a database """

    u_name, p_word = os.getenv("PERSONAL_DATA_DB_USERNAME", "root"), os.getenv('PERSONAL_DATA_DB_PASSWORD', "")
    host, db_name = os.getenv("PERSONAL_DATA_DB_HOST", "localhost"), os.getenv("PERSONAL_DATA_DB_NAME")

    return mysql.connector.connect(host=host, database=db_name, user=u_name, password=p_word)


def main():
    """ a function to get a database connection and get the data stored in a database  and filter it """

    db_connect = get_db()

    db_connect._execute_query("")