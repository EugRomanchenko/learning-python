from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
)
from werkzeug.exceptions import BadRequest

from models import db, Post
from . import crud

posts_app = Blueprint(
    "posts_app",
    __name__,
    url_prefix="/posts"
)


@posts_app.get("/", endpoint="list")
def get_posts_list():
    return render_template(
        "posts/index.html",
        posts=crud.get_posts_list(),
    )


@posts_app.get("/<int:post_id>/", endpoint="details")
def get_post_by_id_or_raise(post_id: int):
    post: Post = crud.get_post_by_id(post_id)

    return render_template(
        "posts/details.html",
        post=post,
    )


@posts_app.route("/create/", endpoint="create", methods=["GET", "POST"])
def create_new_post():
    if request.method == "GET":
        return render_template("posts/create.html", users=crud.get_users_list())

    post_title = request.form.get("post_title")
    if not post_title:
        raise BadRequest("`post_title` field required")

    post_body = request.form.get("post_body")
    if not post_body:
        raise BadRequest("`post_body` field required")

    post_user_name = request.form.get("post_user_name")
    if not post_user_name:
        raise BadRequest("`user_name` field required")

    user = crud.get_user_by_name(user_name=post_user_name)
    post = crud.create_post_by_user(title=post_title, body=post_body, user_id=user.id)
    flash(f"Created post {post.title}", category="success")
    url = url_for("posts_app.details", post_id=post.id)
    return redirect(url)
