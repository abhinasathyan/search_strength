from queries.query import  Query
from web_pages.web_page import Web_page

class Strength_rating:

    def __init__(self,strength_web_page=None,strength_query=None):
        self.strength_web_page=strength_web_page
        self.strength_query=strength_query

    def calculate_strength(self,key,strength_web_page):
        obj_query=Query()
        strength_query=obj_query.list_query[str(key)]
        return (strength_query*strength_web_page)



