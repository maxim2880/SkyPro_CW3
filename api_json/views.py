from flask import Blueprint, render_template, request, jsonify
import logging

from config import POST_PATH
from main.utils import load_json_data, get_post_by_pk

api_json_blueprint = Blueprint("api_json_blueprint", __name__, template_folder="templates")
logging.basicConfig(filename="logger.log", level=logging.INFO)


@api_json_blueprint.route("/api/posts")
def get_json_posts():
    """возвращает полный список постов в виде JSON списка"""
    logging.info("Получен список постов в виде JSON-списка")
    posts = load_json_data(POST_PATH)
    return jsonify(posts)


@api_json_blueprint.route("/api/posts/<post_id>")
def get_json_post(post_id):
    """возвращает один пост в виде JSON словаря"""
    logging.info("Получен пост в виде JSON-списка")
    post = get_post_by_pk(post_id)
    return jsonify(post)
