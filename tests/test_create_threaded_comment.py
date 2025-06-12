import allure

from modules.comment import Comment
from tests.testdata import generate_comment_payload

@allure.tag("functional", "api", "comment")
def test_create_threaded_comment_status_200(new_list_comment):
    comment, payload, comment_id = new_list_comment
    payload = generate_comment_payload()

    response = comment.create_threaded_comment(payload, comment_id)
    threaded_comment_id = response.json()["id"]

    try:
        assert response.status_code == 200, f"Expected 200, got {response.status_code}: {response.text}"
    finally:
        comment.delete_comment(threaded_comment_id)

@allure.tag("functional", "api", "comment")
def test_create_threaded_comment_includes_threaded_comment_id(new_list_comment):
    comment, payload, comment_id = new_list_comment
    payload = generate_comment_payload()

    response = comment.create_threaded_comment(payload, comment_id)
    response_dict = response.json()

    assert "id" in response_dict, f"Missing 'id' in response: {response_dict}"
    assert isinstance(response_dict["id"], int), "Expected 'id' to be an int"

    comment.delete_comment(response_dict["id"])

@allure.tag("functional", "api", "comment")
def test_create_threaded_comment_fails_without_auth(new_list_comment, unauthorized_sender):
    comment, payload, comment_id = new_list_comment
    payload = generate_comment_payload()
    response = Comment(unauthorized_sender).create_threaded_comment(payload, comment_id)

    assert response.status_code == 400, \
        f"Expected 400, got {response.status_code}: {response.text}"