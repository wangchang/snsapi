#-*- encoding: utf-8 -*-

'''
RSS Feed Component

Supported Methods
    * auth() : 
        a NULL stub. 
    * home_timeline() : 
        read and parse RSS feed.
        pretend it to be a 'special' SNS platform, 
        where you can only read your wall but can 
        not write to it.
'''

from ..snsapi import SNSAPI
from ..snstype import Status,User
from ..third import feedparser
#import ..thrid::feedparser

print "RSS Plugged!"

class RSSAPI(SNSAPI):
    def __init__(self):
        super(RSSAPI, self).__init__()
        
        self.platform = "sina"
        self.domain = "api.sina.com"
        #just you remind myself they exists
        self.app_key = ""
        self.app_secret = ""
        #you must set self.plaform before invoking read_config()
        self.read_config()
        
    def auth(self):
        #Nothing to do.
        print "RSS platform do not need auth!"
        
    def home_timeline(self, count=20):
        '''Get home timeline
        get statuses of yours and your friends'
        @param count: number of statuses
        '''

        url = 'http://jason.diamond.name/weblog/feed/'
        d = feedparser.parse(url)
        
        statuslist = []
        for j in d['items']:
            statuslist.append(RSSStatus(j))
        return statuslist

        
class RSSStatus(Status):
    def parse(self, dct):
        self.title = dct['title']
        #self.id = dct["id"]
        #self.created_at = dct["created_at"]
        #self.text = dct['text']
        #self.reposts_count = dct['reposts_count']
        #self.comments_count = dct['comments_count']
        #self.username = dct['user']['name']
        #self.usernick = ""
        
    def show(self):
        #print "[%s] at %s \n  %s" % (self.username, self.created_at, self.text)
        print "%s" % self.title
