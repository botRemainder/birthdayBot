from cgitb import text
from importlib.metadata import files
from webexteamssdk import WebexTeamsAPI
from dotenv import load_dotenv
from pathlib import Path
import os

dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)

# api_token = "XXXXXXX"
# api = WebexTeamsAPI(access_token=api_token)
# msg = api.messages
# msg.create(roomId=None, parentId=None, toPersonId=None, toPersonEmail="xxxxxxx", text="Hi , I am birthday remainder bot")


class WebexSendMsg:
    
    def __init__(self,roomId=None, parentId=None, toPersonId=None, toPersonEmail=None) -> None:
        api_token = os.getenv('WEBEX_API_TOKEN')
        api = WebexTeamsAPI(access_token=api_token)
        self.msg = api.messages
        self.roomId = roomId
        self.parentId = parentId
        self.toPersonId = toPersonId
        self.toPersonEmail = toPersonEmail
        self.text = None
        self.markdown = None
        self.files = None
        self.attachments = None
    
    def createMsg(self,message=None,markdown=None,filedata=None,attachement=None):
        self.msg.create(roomId=self.roomId,parentId=self.parentId,topersonId=self.toPersonId,
                        toPersonEmail=self.toPersonEmail,text=message,markdown=markdown,
                        file=filedata,attachement=attachement)


