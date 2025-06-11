import pytest
from config.settings import *
from modules.comment import Comment
from modules.sender import Sender
from faker import Faker
fake = Faker()

@pytest.fixture
def authorized_sender():
    return Sender(base_url=base_url, auth=api_key)

@pytest.fixture
def unauthorized_sender():
    return Sender(base_url=base_url)

@pytest.fixture
def comment_payload():
    return {
        "comment_text": fake.sentence(),
        "assignee": None,
        "notify_all": True
    }

@pytest.fixture
def new_list_comment(comment_payload, authorized_sender):
    comment = Comment(authorized_sender)

    response = comment.create_list_comment(comment_payload)
    response.raise_for_status()
    comment_id = response.json()["id"]

    yield comment, comment_payload, comment_id

    comment.delete_comment(comment_id)
