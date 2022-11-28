import datetime as dt
import discord
import pyshorteners

import tiktok as tt


class Button():
    type: int
    style: int
    label: str

    def __init__(self):
        self.type = 2
        self.style = 2
        self.label = 'Info'


class Msg:
    """ Msg (social media video source) types:
        - tiktok -> color:0xFE2C55
        - instagram -> color:0x833AB4
        - facebook -> color:0x4267B2
    """

    ogMsg: discord.Message
    video = None
    replyVideo: str = None
    type: str = None
    color: hex = None
    content: str = None
    button: Button = None
    created: dt.datetime = dt.datetime.now()

    def __init__(self, message):
        try:
            self.errCode = 1
            self.ogMsg = message
            self.msgSorting()
            if self.type:
                self.colors()
                self.msgContent()

        except Exception as e:
            if e:
                print(f"{self.errCode} - ERROR: {e}")
            else:
                print(f"{self.errCode} - ERROR: No content in '{message.content}'")

    def msgSorting(self):
        self.errCode = 1
        if 'tiktok.com' in self.ogMsg.content:
            self.type = 'tiktok'
        elif 'instagram.com' in self.ogMsg.content:
            self.type = 'instagram'
        elif 'facebook.com' in self.ogMsg.content:
            self.type = 'facebook'
        else:
            self.type = None

    def colors(self):
        self.errCode = 2
        match self.type:
            case 'tiktok':
                self.color = 0xFE2C55
            case 'instagram':
                self.color = 0x833AB4
            case 'facebook':
                self.color = 0x4267B2

    def msgContent(self):
        self.errCode = 3
        self.content = ""
        for item in self.ogMsg.content.split(' '):
            if self.type in item:
                self.content += f"<{item}>" + " "
            else:
                self.content += item + " "

    def getVideo(self):
        self.errCode = 4
        match self.type:
            case 'tiktok':
                self.video = tt.TikTok(self.ogMsg.content)
            case 'instagram':
                self.video = None
            case 'facebook':
                self.video = None
        self.urlShortener()

    def urlShortener(self):
        self.errCode = 5

        type_tiny = pyshorteners.Shortener()
        self.replyVideo = type_tiny.tinyurl.short(self.video.videoLink)
