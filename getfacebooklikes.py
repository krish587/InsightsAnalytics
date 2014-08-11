""" This program used to get likes of fb page please add the username in if main function get the likes. output will be in csv format """

import csv
import urllib2
from collections import OrderedDict
from urllib2 import urlopen
from json import load
import time
import json
class GraphSearch:
    def __init__(self,userlist):
        self.userslist = userlist
        pass

    def __get_graph_search_details__(self,username):
        url = "http://graph.facebook.com/"+username        
        fbpagedata = urlopen(url)
        jsondata = json.load(fbpagedata)        
        try:
            likes,category,about = jsondata['likes'],jsondata['category'],json['about']
        except Exception,e:
            likes,category,about = (None,None,None)
        return likes,category,about

    def __get_user_likes__(self):

        with open('fblikes.csv', 'wb') as csvfile:
            csv_writer = csv.writer(csvfile,delimiter="|")
            for username in self.userslist:
                print username
                category,likes,about = self.__get_graph_search_details__(username)
                time.sleep(1)
                csv_writer.writerow([category,likes,about])
    
    

if __name__=="__main__":
    
    userslist = ['presidentkalam','VivekanandaPage','1BhagatSingh']
    GS = GraphSearch(userslist)
    GS.__get_user_likes__()
