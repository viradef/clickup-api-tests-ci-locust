from modules.comment import Comment

def test_delete_comment_status_200(new_list_comment):
    comment, payload, comment_id = new_list_comment
    response = comment.delete_comment(comment_id)
    assert response.status_code == 200, \
        f"Expected 200, got {response.status_code}: {response.text}"

def test_delete_comment_fails_without_auth(new_list_comment, unauthorized_sender):
    comment, payload, comment_id = new_list_comment
    response = Comment(unauthorized_sender).delete_comment(comment_id)
    assert response.status_code == 400, \
        f"Expected 400, got {response.status_code}: {response.text}"