import json

from config import COMMENT_PATH, POST_PATH, BOOKMARK_PATH
from exceptions import *


def load_json_data(path):
    """Загрузка информации из Json файла"""
    try:
        with open(path, 'r', encoding="UTF-8") as file:
            return json.load(file)
    except(FileNotFoundError, json.JSONDecodeError):
        raise DataJsonError


def get_comments_by_post_id(post_id):
    """возвращает комментарии определенного поста"""
    comments_to_post = []
    try:
        comments = load_json_data(COMMENT_PATH)
        for comment in comments:
            if str(post_id) == str(comment["post_id"]):
                comments_to_post.append(comment)
        return comments_to_post
    except:
        print("Номер поста должены быть целым положительным числом")


def get_post_by_pk(pk):
    """возвращает один пост по его идентификатору"""
    posts = load_json_data(POST_PATH)
    try:
        for post in posts:
            if str(pk) == str(post["pk"]):
                return post
    except:
        print("Номер поста должены быть целым положительным числом")


def get_posts_by_user(user_name):
    """возвращает посты определенного пользователя"""
    posts_by_user = []
    user_posts = create_hashtag_dict()
    for user_post in user_posts:
        if user_name.lower() == user_post["poster_name"]:
            posts_by_user.append(user_post)
    return posts_by_user


def search_for_posts(query):
    """возвращает список постов по ключевому слову"""
    posts_by_query = []
    user_posts = load_json_data(POST_PATH)
    for user_post in user_posts:
        if query.lower() in user_post["content"].lower():
            posts_by_query.append(user_post)
    return posts_by_query


def search_by_hashtag(hashtag):
    """Функция для поиска постов по хэштегу"""
    post_by_hashtag = []
    user_posts = create_hashtag_dict()
    for post in user_posts:
        if post["content"].split(" ")[0][1:] == hashtag:
            post_by_hashtag.append(post)
    return post_by_hashtag


def create_hashtag_dict():
    """Функция искусственного добавления ключа "хэштег" в json"""
    posts = load_json_data(POST_PATH)
    for post in posts:
        if "#" in post["content"].split(" ")[0]:
            post["hashtag"] = post["content"].split(" ")[0][1:]
        else:
            post["hashtag"] = ""
    return posts


def add_post_by_id(pk):
    """Функция добавляет 1 пост в json файл"""
    posts = load_json_data(POST_PATH)
    bookmarks = load_json_data(BOOKMARK_PATH)
    try:
        for post in posts:
            if str(pk) == str(post["pk"]):
                if post in bookmarks:
                    return "Пост уже есть в закладках"
                bookmarks.append(post)
                with open(BOOKMARK_PATH, "w", encoding="utf-8") as file:
                    json.dump(bookmarks, file)
                return bookmarks
    except:
        print("Номер поста должены быть целым положительным числом")


def remove_post_by_id(pk):
    """Функция удаляет 1 пост из json файл"""
    posts = load_json_data(POST_PATH)
    bookmarks = load_json_data(BOOKMARK_PATH)
    if not bookmarks:
        return "Закладки отсуствуют"
    try:
        for post in posts:
            if str(pk) == str(post["pk"]):
                if post not in bookmarks:
                    return "Пост отсутствует в закладках"
                bookmarks.remove(post)
                with open(BOOKMARK_PATH, "w", encoding="utf-8") as file:
                    json.dump(bookmarks, file)
                return bookmarks
    except:
        print("Номер поста должены быть целым положительным числом")

