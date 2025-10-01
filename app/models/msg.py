from datetime import datetime
from .. import db


class Msg(db.Model):
    __tablename__ = "chat_msgs"
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, nullable=False)
    receiver_id = db.Column(db.Integer, nullable=False)
    message = db.Column(db.String(255), nullable=False)
    created_at = db.Column(
        db.Integer, default=lambda: int(datetime.now().timestamp()), nullable=False
    )

    def to_dict(self):
        return {
            "id": self.id,
            "sender_id": self.sender_id,
            "receiver_id": self.receiver_id,
            "message": self.message,
            "created_at": (
                datetime.fromtimestamp(self.created_at).strftime("%Y-%m-%d")
                if self.created_at
                else None
            ),
        }

    def __repr__(self):
        return f"<Users {self.id}>"
