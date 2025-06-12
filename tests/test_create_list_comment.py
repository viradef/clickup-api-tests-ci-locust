from modules.comment import Comment

def test_create_list_comment_status_200(comment_payload, authorized_sender):
    comment = Comment(authorized_sender)

    response = comment.create_list_comment(comment_payload)
    comment_id = response.json()["id"]

    try:
        assert response.status_code == 200, \
            f"Expected 200, got {response.status_code}: {response.text}"
    finally:
        comment.delete_comment(comment_id)

def test_create_comment_response_includes_comment_id(comment_payload, authorized_sender):
    comment = Comment(authorized_sender)
    response = comment.create_list_comment(comment_payload)

    response_dict = response.json()
    assert "id" in response_dict, f"Missing 'id' in response: {response_dict}"
    assert isinstance(response_dict["id"], int), "Expected 'id' to be an int"

    comment.delete_comment(response_dict["id"])

def test_create_list_comment_fails_without_auth(comment_payload, unauthorized_sender):
    response = Comment(unauthorized_sender).create_list_comment(comment_payload)
    assert response.status_code == 400, \
        f"Expected 400, got {response.status_code}: {response.text}"