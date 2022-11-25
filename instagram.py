class Insta:
    url: str
    data: str = None
    videoLink: str = None
    videoTitle: str = None
    videoDescription: str = None
    videoStats: str = None
    videoAuthor: str = None

    def __init__(self, message):
        try:
            self.errCode = 1
            self.ogMsg = message
            # self.msgSorting()
            # if self.type:
            #     self.colors()
            #     self.msgContent()
            #     self.getVideo()

        except Exception as e:
            if e:
                print(f"{self.errCode} - ERROR: {e}")
            else:
                print(f"{self.errCode} - ERROR: No content in '{message.content}'")

