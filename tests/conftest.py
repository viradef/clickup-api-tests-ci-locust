import pytest
from config.settings import *
from modules.comment import Comment
from modules.sender import Sender
from tests.testdata import generate_comment_payload
from faker import Faker

fake = Faker()

@pytest.fixture
def authorized_sender():
    return Sender(base_url=base_url, auth=api_key)

@pytest.fixture
def unauthorized_sender():
    return Sender(base_url=base_url)


@pytest.fixture(scope="function")
def new_list_comment(authorized_sender):
    comment = Comment(authorized_sender)
    comment_payload = generate_comment_payload()
    response = comment.create_list_comment(comment_payload)
    response.raise_for_status()
    comment_id = response.json()["id"]

    yield comment, comment_payload, comment_id

    comment.delete_comment(comment_id)

@pytest.fixture(scope="function")
def new_task_comment(authorized_sender):
    comment = Comment(authorized_sender)
    comment_payload = generate_comment_payload()
    response = comment.create_task_comment(comment_payload)
    response.raise_for_status()
    comment_id = response.json()["id"]

    yield comment, comment_payload, comment_id

    comment.delete_comment(comment_id)