from modules.comment import Comment

def test_get_task_comments_status_200(authorized_sender):
    response = Comment(authorized_sender).get_task_comments()
    assert response.status_code == 200,\
        f"Expected 200, got {response.status_code}: {response.text}"

def test_get_task_comments_fails_without_auth(unauthorized_sender):
    response = Comment(unauthorized_sender).get_task_comments()
    assert response.status_code == 400,\
        f"Expected 400, got {response.status_code}: {response.text}"

def test_get_task_comments_returns_created_comment_data_fields(new_task_comment):
    comment, payload, comment_id = new_task_comment

    task_comments = comment.get_task_comments().json()["comments"]
    matched_comment = next((item for item in task_comments if item["id"] == str(comment_id)), None)

    assert matched_comment is not None, \
        f"Comment ID {comment_id} not found in comments: {[i['id'] for i in task_comments]}"

    assert matched_comment["comment_text"] == payload["comment_text"],\
        f"Expected comment text: {payload['comment_text']}, got: {matched_comment['comment_text']}"

    assert matched_comment["assignee"] == payload["assignee"], \
        f"Expected comment assignee: {payload['assignee']}, got: {matched_comment['assignee']}"