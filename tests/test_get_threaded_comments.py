from http.client import responses

import allure

from modules.comment import Comment

@allure.tag("functional", "api", "comment")
def test_get_threaded_comments_status_200(new_list_comment):
    comment, payload, comment_id = new_list_comment

    response = comment.get_threaded_comments(comment_id)
    assert response.status_code == 200,\
        f"Expected 200, got {response.status_code}: {response.text}"

@allure.tag("functional", "api", "comment")
def test_get_threaded_comments_fails_without_auth(new_list_comment, unauthorized_sender):
    comment, payload, comment_id = new_list_comment

    response = Comment(unauthorized_sender).get_threaded_comments(comment_id)
    assert response.status_code == 400, \
        f"Expected 400, got {response.status_code}: {response.text}"

@allure.tag("functional", "api", "comment")
def test_get_threaded_comments_returns_created_comment_data(new_list_comment):
    comment, payload, comment_id = new_list_comment

    response = comment.create_threaded_comment(payload, comment_id)
    threaded_comment_id = response.json()["id"]

    threaded_comments = comment.get_threaded_comments(comment_id).json()["comments"]
    matched_comment = next((item for item in threaded_comments if str(item["id"]) == str(threaded_comment_id)), None)

    assert matched_comment is not None, \
        f"Comment ID {threaded_comment_id} not found in comments: {[i['id'] for i in threaded_comments]}"

    assert matched_comment["comment_text"] == payload["comment_text"], \
        f"Expected comment text: {payload['comment_text']}, got: {matched_comment['comment_text']}"