from modules.comment import Comment

def test_get_list_comments_status_200(authorized_sender):
    response = Comment(authorized_sender).get_list_comments()
    assert response.status_code == 200, f"Expected 200, got {response.status_code}: {response.text}"