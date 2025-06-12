from modules.comment import Comment
from tests.testdata import generate_comment_payload

def test_create_list_comment_status_200(authorized_sender):
    comment = Comment(authorized_sender)
    payload = generate_comment_payload()

    response = comment.create_list_comment(payload)
    comment_id = response.json()["id"]

    try:
        assert response.status_code == 200, \
            f"Expected 200, got {response.status_code}: {response.text}"
    finally:
        comment.delete_comment(comment_id)

def test_create_list_comment_response_includes_comment_id(authorized_sender):
    comment = Comment(authorized_sender)
    payload = generate_comment_payload()

    response = comment.create_list_comment(payload)
    response_dict = response.json()

    assert "id" in response_dict, f"Missing 'id' in response: {response_dict}"
    assert isinstance(response_dict["id"], int), "Expected 'id' to be an int"

    comment.delete_comment(response_dict["id"])

def test_create_list_comment_fails_without_auth(unauthorized_sender):
    payload = generate_comment_payload()
    response = Comment(unauthorized_sender).create_list_comment(payload)
    assert response.status_code == 400, \
        f"Expected 400, got {response.status_code}: {response.text}"