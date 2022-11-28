import requests
from bs4 import BeautifulSoup
import json
import misc
import logging

class TikTok:
    url: str
    data: str = None
    videoLink: str = None
    videoTitle: str = None
    videoDescription: str = None
    videoStats: str = None
    videoAuthor: str = None

    def __init__(self, url):
        self.url = url
        self.getData()
        self.getVideo()

    def getData(self):
        logging.basicConfig(format = '%(asctime)s %(levelname)-8s %(message)s',level=logging.DEBUG, datefmt = '%Y-%m-%d %H:%M:%S')
        r = requests.get(self.url,
            headers={
                'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'},
            timeout=30)
        self.data = r.text

        html = BeautifulSoup(self.data, 'html.parser')
        self.videoTitle = html.head.title.string

    def parseData(self):
        html = BeautifulSoup(self.data, 'html.parser')
        self.videoDescription = html.find(attrs={"property": "og:description"})['content']
        meta = html.find(attrs={"name": "description"})['content']
        self.videoStats = meta.split('TikTok video from')[0]
        self.videoAuthor = meta.split('TikTok video from ')[1].split('):')[0] + ')'

    def getVideo(self):
        if self.videoTitle != "TikTok - Make Your Day":
            html = BeautifulSoup(self.data, 'html.parser')
            script = json.loads(html.find(id='SIGI_STATE').string)
            for item in misc.jsonFindAttr('playAddr', script):
                self.videoLink = item
        else:
            self.videoLink = 'https://cdn.discordapp.com/attachments/928687829284954165/1043936740555108522/unknown.png'
