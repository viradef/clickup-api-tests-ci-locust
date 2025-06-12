from locust import task, TaskSet
from config.settings import api_key, list_id, task_id
from tests.testdata import generate_comment_payload
import random

class CommentTasks(TaskSet):
    def on_start(self):
        self.comment_ids = []
        self.headers = {
            "Authorization": api_key,
            "Content-Type": "application/json"
        }

        payload = generate_comment_payload()
        with self.client.post(f"/api/v2/list/{list_id}/comment", json=payload, headers=self.headers, catch_response=True) as response:
            if response.status_code == 200:
                self.comment_ids.append(response.json()["id"])
            else:
                response.failure(f"Failed to create comment at start: {response.text}")

    @task(3)
    def get_list_comments(self):
        self.client.get(f"/api/v2/list/{list_id}/comment", headers=self.headers)

    @task(2)
    def create_list_comment(self):
        payload = generate_comment_payload()
        with self.client.post(f"/api/v2/list/{list_id}/comment", json=payload, headers=self.headers, catch_response=True) as response:
            if response.status_code == 200:
                self.comment_ids.append(response.json()["id"])
            else:
                response.failure(f"Failed to create comment: {response.text}")

    @task(1)
    def update_comment(self):
        if not self.comment_ids:
            return
        comment_id = random.choice(self.comment_ids)
        payload = generate_comment_payload()
        with self.client.put(f"/api/v2/comment/{comment_id}", json=payload, headers=self.headers, catch_response=True) as response:
            if response.status_code != 200:
                response.failure(f"Failed to update comment {comment_id}: {response.text}")

    @task(1)
    def delete_comment(self):
        if not self.comment_ids:
            return
        comment_id = self.comment_ids.pop()
        with self.client.delete(f"/api/v2/comment/{comment_id}", headers=self.headers, catch_response=True) as response:
            if response.status_code != 200:
                response.failure(f"Failed to delete comment {comment_id}: {response.text}")
