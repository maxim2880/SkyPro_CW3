import requests


def test_check_status_code_equals_200():
    """Тест корректного статуса ответа сервера"""
    response_posts = requests.get("http://127.0.0.1:5000/api/posts")
    response_post = requests.get("http://127.0.0.1:5000/api/posts/1")
    assert response_posts.status_code == 200
    assert response_post.status_code == 200


def test_check_type_json():
    """Проверка типа возвращаемого ответа сервера"""
    response_posts = requests.get("http://127.0.0.1:5000/api/posts").json()
    response_post = requests.get("http://127.0.0.1:5000/api/posts/1").json()
    assert type(response_posts) == list
    assert type(response_post) == dict


def test_check_key_json():
    """Проверка набора ключей в ответе сервера"""
    list_of_keys = ["poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"]
    response_posts = requests.get("http://127.0.0.1:5000/api/posts").json()
    response_post = requests.get("http://127.0.0.1:5000/api/posts/1").json()
    for key in response_posts[0]:
        assert key in list_of_keys
    for key in response_post:
        assert key in list_of_keys








