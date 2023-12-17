from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
)
from werkzeug.exceptions import BadRequest

from models import db, Post, User
from . import crud

users_app = Blueprint(
    "users_app",
    __name__,
    url_prefix="/users"
)


@users_app.get("/", endpoint="list")
def get_users_list():
    return render_template(
        "users/index.html",
        users=crud.get_users_list(),
    )


@users_app.get("/<int:user_id>/", endpoint="details")
def get_user_by_id_or_raise(user_id: int):
    user: User = crud.get_user_by_id(user_id)

    return render_template(
        "users/details.html",
        user=user,
    )


@users_app.route("/create/", endpoint="create", methods=["GET", "POST"])
def create_new_user():
    if request.method == "GET":
        return render_template("users/create.html")

    user_name = request.form.get("user_name")
    if not user_name:
        raise BadRequest("`user_name` field required")

    user_username = request.form.get("user_username")
    if not user_username:
        raise BadRequest("`user_username` field required")

    user_email = request.form.get("user_email")

    user = crud.create_user(name=user_name, username=user_username, email=user_email)
    flash(f"Created user {user_name}", category="success")
    url = url_for("users_app.details", user_id=user.id)
    return redirect(url)
