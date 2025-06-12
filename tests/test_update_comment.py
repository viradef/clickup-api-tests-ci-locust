import allure
import pytest
from modules.comment import Comment
from tests.testdata import update_comment_text_cases, generate_random_sentence

@allure.tag("functional", "api", "comment", "parametrized")
@pytest.mark.parametrize("new_comment_text, expected_status", update_comment_text_cases)
def test_update_comment_text_status_code(new_list_comment, new_comment_text, expected_status):
    comment, payload, comment_id = new_list_comment
    payload["comment_text"] = new_comment_text

    response = comment.update_comment(payload, comment_id)
    assert response.status_code == expected_status, \
        f"Expected {expected_status}, got {response.status_code}: {response.text}"

@allure.tag("functional", "api", "comment", "parametrized")
@pytest.mark.parametrize("new_comment_text, expected_status", update_comment_text_cases)
def test_comment_text_is_updated_successfully(new_list_comment, new_comment_text, expected_status):
    comment, payload, comment_id = new_list_comment
    payload["comment_text"] = new_comment_text

    comment.update_comment(payload, comment_id)
    list_comments = comment.get_list_comments().json()["comments"]
    matched_comment = next((item for item in list_comments if item["id"] == str(comment_id)), None)

    assert matched_comment is not None, \
        f"Comment ID {comment_id} not found in comments: {[i['id'] for i in list_comments]}"

    assert matched_comment["comment_text"] == payload["comment_text"], \
        f"Expected comment text: {payload['comment_text']}, got: {matched_comment['comment_text']}"

@allure.tag("functional", "api", "comment")
def test_update_comment_fails_without_auth(new_list_comment, unauthorized_sender):
    comment, payload, comment_id = new_list_comment
    payload["comment_text"] = generate_random_sentence()

    response = Comment(unauthorized_sender).update_comment(payload, comment_id)
    assert response.status_code == 400,\
        f"Expected 400, got {response.status_code}: {response.text}"