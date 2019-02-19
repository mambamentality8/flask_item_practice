from flask import current_app
from flask import session

from info.models import User
from . import index_blu

from flask import render_template

@index_blu.route('/')
def index():
    # 获取到当前登录用户的id
    user_id = session.get("user_id")
    # 通过id获取用户信息
    user = None
    if user_id:
        try:
            user = User.query.get(user_id)
        except Exception as e:
            current_app.logger.error(e)

    return render_template('news/index.html', data={"user_info": user.to_dict() if user else None})