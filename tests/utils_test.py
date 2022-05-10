import json

import pytest

from main.utils import load_json_data, get_comments_by_post_id, get_post_by_pk, get_posts_by_user, search_for_posts


def test_load_json_data():
    """Тестирование функции выгрузки информации из файла json"""
    with pytest.raises(FileNotFoundError):
        load_json_data()
    with pytest.raises(json.JSONDecodeError):
        load_json_data(123)


def test_get_comments_by_post_id():
    """тестирование функции получения комментариев к посту"""
    with pytest.raises(TypeError):
        get_comments_by_post_id(-1)
    assert get_comments_by_post_id(1) == list


def test_get_post_by_pk():
    """тестирование функции получения одного поста по его номеру"""
    with pytest.raises(TypeError):
        get_post_by_pk(-1)
    assert get_post_by_pk(1) == list


def test_get_posts_by_user():
    """тестирование функции получения получения постов пользователя"""
    with pytest.raises(TypeError):
        get_post_by_pk(-1)
    assert get_post_by_pk(1) == list

