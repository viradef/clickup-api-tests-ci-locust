from locust import HttpUser, between
from tasks.comment_tasks import CommentTasks

class CommentUser(HttpUser):
    tasks = [CommentTasks]
    wait_time = between(3, 6)  # Wait between requests
    host = "https://api.clickup.com"