from config.settings import *
from modules.sender import Sender

class Comment:
    def __init__(self, sender: Sender, custom_list_id: str | None = None):
        self.sender = sender
        self.list_id = custom_list_id or list_id

    def get_list_comments(self):
        path = f"/list/{list_id}/comment"
        return self.sender.get(path)