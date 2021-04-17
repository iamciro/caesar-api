"""
This file contains utils functions
"""

def get_quotes_from_file(filename):
    quotes = []
    with open(filename, "r") as quotes_file:
        for quote in quotes_file:
            quote = quote.replace('\n', '')
            quotes.append(quote)
    return quotes