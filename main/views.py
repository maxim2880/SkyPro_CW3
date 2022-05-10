from flask import Blueprint, render_template, request, jsonify
import logging

from werkzeug.utils import redirect

from config import POST_PATH, BOOKMARK_PATH
from main.utils import load_json_data, get_comments_by_post_id, get_post_by_pk, get_posts_by_user, search_for_posts, \
    search_by_hashtag, create_hashtag_dict, add_post_by_id, remove_post_by_id

main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")

logging.basicConfig(filename="logger.log", level=logging.INFO)


@main_blueprint.route("/")
def main_page():
    """Открытие главной страницы с шаблоном index.html"""
    logging.info("Открытие главной страницы")
    posts = create_hashtag_dict()
    return render_template("index.html", posts=posts)


@main_blueprint.route("/posts/<post_id>")
def posts_view(post_id):
    """Возвращает список комментариев к выбранному посту"""
    logging.info("Вывод комментариев к посту")
    comments = get_comments_by_post_id(post_id)
    comments_count = len(comments)
    post = get_post_by_pk(post_id)
    return render_template("post.html", comments=comments, post=post, comments_count=comments_count)


@main_blueprint.route("/users/<username>")
def posts_by_user(username):
    """Возвращает все посты пользователя"""
    logging.info("Выполняется поиск постов пользователя")
    posts = get_posts_by_user(username)
    ava = posts[0]['poster_avatar']
    return render_template("user-feed.html", posts=posts, username=username, ava=ava)


@main_blueprint.route('/search')
def search_page():
    """Возвращает список постов по ключевому слову"""
    s = request.args.get("s", "")
    logging.info("Выполняется поиск")
    posts_by_query = search_for_posts(s)
    number_of_posts = len(posts_by_query)
    return render_template("search.html", posts=posts_by_query, s=s, number=number_of_posts)


@main_blueprint.route("/tag/<tagname>")
def posts_by_hashtag(tagname):
    """Возвращает все посты с выбранным тегом"""
    posts = search_by_hashtag(tagname)
    return render_template("tag.html", posts=posts, tag=tagname)


@main_blueprint.route('/bookmarks/add/<postid>', methods=["POST", "GET"])
def add_page(postid):
    """Добавляет выбранный пост в закладки"""
    add_post_by_id(postid)
    return redirect("http://127.0.0.1:5000/", code = 302)


@main_blueprint.route('/bookmarks/remove/<postid>', methods=["POST", "GET"])
def remove_page(postid):
    """Удаляет выбранный пост из закладок"""
    posts = remove_post_by_id(postid)
    return redirect("http://127.0.0.1:5000/", code=302)


@main_blueprint.route('/bookmarks')
def show_bookmarks():
    """Выводит все закладки"""
    posts = load_json_data(BOOKMARK_PATH)
    count_bookmarks = len(posts)
    return render_template("bookmarks.html", posts=posts, count_bookmarks=count_bookmarks)
