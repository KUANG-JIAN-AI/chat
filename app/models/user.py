from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from .. import db


class Users(db.Model):
    __tablename__ = "chat_users"
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(
        db.Integer, default=lambda: int(datetime.now().timestamp()), nullable=False
    )
    updated_at = db.Column(
        db.Integer,
        default=lambda: int(datetime.now().timestamp()),
        onupdate=lambda: int(datetime.now().timestamp()),
        nullable=False,
    )
    deleted_at = db.Column(db.Integer, nullable=True)

    def set_password(self, password: str):
        self.password = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            "id": self.id,
            "nickname": self.nickname,
            "created_at": (
                datetime.fromtimestamp(self.created_at).strftime("%Y-%m-%d")
                if self.created_at
                else None
            ),
            "updated_at": (
                datetime.fromtimestamp(self.updated_at).strftime("%Y-%m-%d")
                if self.updated_at
                else None
            ),
        }

    def __repr__(self):
        return f"<Users {self.id}>"
