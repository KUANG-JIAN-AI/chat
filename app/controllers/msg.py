from flask import current_app, request
from sqlalchemy import and_, or_

from app.models.msg import Msg, db


def send_msg():
    data = request.get_json()  # 从请求体里解析 JSON
    sender_id = data.get("sender_id")
    receiver_id = data.get("receiver_id")
    message = data.get("message")

    with current_app.app_context():
        if not sender_id or not receiver_id or not message:
            return {"code": 400, "msg": "missing"}

        msg = Msg(sender_id=sender_id, receiver_id=receiver_id, message=message)

        with current_app.app_context():
            db.session.add(msg)
            db.session.commit()

        return {"code": 200, "msg": "success"}


def get_msg():
    sender_id = request.args.get("sender_id")
    receiver_id = request.args.get("receiver_id")
    msgs = Msg.query.filter(
        or_(
            and_(Msg.sender_id == sender_id, Msg.receiver_id == receiver_id),
            and_(Msg.sender_id == receiver_id, Msg.receiver_id == sender_id),
        )
    ).all()
    return {"code": 200, "msg": "success", "data": [m.to_dict() for m in msgs]}
