from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from .database import db


class User(db.Model):

    __tablename__ = 'users'

    name = Column(String(32), nullable=False, unique=True)
    username = Column(String(32), nullable=False, unique=True)
    email = Column(String, nullable=True, unique=True)

    posts = relationship(
        "Post",
        back_populates="user",
        uselist=True,
    )

    def __str__(self):
        return (
            f"{self.__class__.__name__}(id={self.id}, "
            f"username={self.username!r}, email={self.email!r}"
        )

    def __repr__(self):
        return str(self)