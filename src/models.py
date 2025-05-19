from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    firstname: Mapped[str] = mapped_column(String(20), nullable=False)
    lastname: Mapped[str] = mapped_column(String(20), nullable=False)
    username: Mapped[str] = mapped_column(String(30), nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Post (db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int]=mapped_column(db.ForeignKey("user.id"))
    user=db.relationship("User", backref="posts") 

class Media  (db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(String(30), nullable=False)
    url:  Mapped[str] = mapped_column(String(100), nullable=False)
    post_id: Mapped[int]=mapped_column(db.ForeignKey("post.id"))
    post= db.relationship("Post", backref="media")

class Comment (db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    comment_text: Mapped[str] = mapped_column(String(100), nullable=False)
    author_id: Mapped[int]=mapped_column(db.ForeignKey("user.id"))
    author= db.relationship("User", backref="comments")
    post_id: Mapped[int]=mapped_column(db.ForeignKey("post.id"))
    post= db.relationship("Post", backref="comments")

class Follower (db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_from_id: Mapped[int]=mapped_column(db.ForeignKey("user.id"))
    user_from = db.relationship("User", backref="followers")
    user_to_id: Mapped[int]=mapped_column(db.ForeignKey("user.id"))
    user_to = db.relationship("User", backref="followers")



