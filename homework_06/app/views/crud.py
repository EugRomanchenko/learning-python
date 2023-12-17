from models import db, Post, User


def get_posts_list() -> list[Post]:
    return Post.query.all()


def get_users_list() -> list[User]:
    return User.query.all()


def get_post_by_id(post_id: int) -> Post:
    return Post.query.get_or_404(
        post_id,
        f"product #{post_id} not found",
    )


def get_user_by_id(user_id: int) -> User:
    return User.query.get_or_404(
        user_id,
        f"user #{user_id} not found",
    )


def get_user_by_name(user_name: str) -> User:
    return db.one_or_404(db.select(User).filter_by(name=user_name))


def create_user(name: str, username: str, email: str | None = None) -> User:
    user = User(
        name=name,
        username=username,
        email=email,
    )
    db.session.add(user)
    db.session.commit()
    return user


def create_post_by_user(title: str, body: str, user_id: int) -> Post:
    post = Post(
        title=title,
        body=body,
        user_id=user_id,
    )
    db.session.add(post)
    db.session.commit()
    return post
