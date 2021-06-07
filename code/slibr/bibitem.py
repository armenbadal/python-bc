import json

class BibItem:
    def __init__(self):
        self.number = 0

#
class ItemEncoder(json.JSONEncoder):
    def default(self, item):
        if isinstance(item, Book) or isinstance(item, Magazine):
            return item.__dict__
        
        return json.JSONDecoder.default(self, item)

# 
def asJson(item):
    return ItemEncoder().encode(item)



# Գիրք
class Book(BibItem):
    def __init__(self, author, title, publ, year):
        self.__book__ = True
        self.author = author
        self.title = title
        self.publisher = publ
        self.year = year


# Ամսագիր
class Magazine(BibItem):
    def __init__(self, title, year, issue):
        self.__magazine__ = True
        self.title = title
        self.year = year
        self.issue = issue

