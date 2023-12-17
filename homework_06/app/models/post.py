from sqlalchemy import Column, String, Integer, Text, UniqueConstraint, ForeignKey
from sqlalchemy.orm import relationship
from .database import db


class Post(db.Model):

    __tablename__ = 'posts'
    __table_args__ = (
        UniqueConstraint("title", "body"),
    )

    title = Column(
        String(100),
        nullable=False,
        default="",
        server_default="",
    )

    body = Column(
        Text,
        nullable=False,
        default="",
        server_default="",
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        unique=False,
        nullable=False,
    )

    user = relationship(
        "User",
        back_populates="posts",
        uselist=False,
    )

    def __str__(self):
        return (
            f"{self.__class__.__name__}(id={self.id}, "
            f"title={self.title!r}, user_id={self.user_id!r}"
        )

    def __repr__(self):
        return str(self)