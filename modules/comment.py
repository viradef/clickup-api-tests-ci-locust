from config.settings import *
from modules.sender import Sender

class Comment:
    def __init__(self, sender: Sender, custom_list_id: str | None = None):
        self.sender = sender
        self.list_id = custom_list_id or list_id

    def get_list_comments(self):
        path = f"/list/{list_id}/comment"
        return self.sender.get(path)

    def create_list_comment(self, payload):
        path = f"/list/{list_id}/comment"
        return self.sender.post(path, payload)

    def delete_comment(self, comment_id):
        path = f"/comment/{comment_id}"
        return self.sender.delete(path)

    def update_comment(self, payload, comment_id):
        path = f"/comment/{comment_id}"
        return self.sender.put(path, payload)