"""
Routes configs
"""
import os
from flask import Blueprint, request, jsonify
from app.models import db, Like, Comment
from datetime import datetime
from app.cache_config import cache

main = Blueprint("main", __name__)

ALLOWED_IPS = os.getenv('ALLOWED_IPS').split(',')

@main.before_request
def limit_remote_addr():
    """
    Limit access for allowed Ips
    """
    if request.remote_addr not in ALLOWED_IPS:
        return jsonify({"error": "Forbidden"}), 403

@main.route("/endpoint/like", methods=["POST"])
def like():
    """
    Store like action info
    """
    data = request.json
    new_like = Like(
        timestamp=datetime.utcnow(),
        email=data.get("email"),
        name=data.get("name"),
        origin=data.get("origin"),
        page_slug=data.get("page_slug"),
    )
    db.session.add(new_like)
    db.session.commit()
    return jsonify({"message": "Like added successfully"}), 201

@main.route("/endpoint/comment", methods=["POST"])
def comment():
    """
    Store comment action info
    """
    data = request.json
    new_comment = Comment(
        timestamp=datetime.utcnow(),
        email=data.get("email"),
        name=data.get("name"),
        origin=data.get("origin"),
        page_slug=data.get("page_slug"),
        content=data.get("content"),
    )
    db.session.add(new_comment)
    db.session.commit()
    return jsonify({"message": "Comment added successfully"}), 201

@main.route("/endpoint/interactions", methods=["GET"])
@cache.cached(timeout=50)
def get_interactions():
    """
    List interactions
    """
    origin = request.args.get("origin")
    page_slug = request.args.get("page_slug")

    like_count = Like.query.filter_by(origin=origin, page_slug=page_slug).count()
    comment_count = Comment.query.filter_by(origin=origin, page_slug=page_slug).count()

    return jsonify({
        "like_count": like_count,
        "comment_count": comment_count
    }), 200
