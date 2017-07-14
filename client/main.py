from parser import Parser
from queries.query import Query
from web_pages.web_page import Web_page
from strength_rating import Strength_rating
while(True):
    command=input().lower()
    if(len(command)==0):
        break
    else:
        strength=0
        obj_parse=Parser()
        obj_web_page=Web_page()
        obj_query=Query()
        obj_strength=Strength_rating()
        parsed=(obj_parse.split(command))
        lenght=len(parsed)
        i=1

        if(parsed[0]=='p'):
            while i<lenght:
                obj_web_page.list_web_page.append(parsed[i])
                i+=1

        if(parsed[0]=='q'):
            while i<lenght:
                obj_query.list_query.append(parsed[i])
        print(obj_web_page.list_web_page)
        print(obj_query.list_query)
