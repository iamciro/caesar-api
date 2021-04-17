"""
This file contains utils functions
"""
from flask import abort

def get_quotes_from_file(filename):
    '''
        Return a list of quotes from a given file. 
    '''
    quotes = []
    try:
        with open(filename, "r") as quotes_file:
            for quote in quotes_file:
                quote = quote.replace('\n', '')
                quotes.append(quote)
        return quotes
    except FileNotFoundError:
        abort(500, "File not found")