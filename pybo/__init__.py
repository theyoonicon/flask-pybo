# pybo.py 와 pybo/__init__.py는 동일한 pybo 모듈이다.

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

import config

naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate()

# 함수명으로 create_app 대신 다른 이름을 사용하면 정상으로 동작하지 않는다. create_app은 플라스크 내부에서 정의된 함수명이다.
def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    
    # ORM
    db.init_app(app)
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)
    from . import models
    
    # blue print
    from .views import main_views, question_views, answer_views, auth_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    app.register_blueprint(auth_views.bp)
    
    # 필터
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime
    
    return app

# flask run 명령은 반드시 프로젝트 홈 디렉터리(C:/projects/myproject)에서 실행해야한다.
# 다른 곳에서 실행하면 실행은 되지만 정상으로 동작하지 않는다. 앞으로도 flask run으로 플라스크 서버를 실행할 때는 위치를 꼭 확인하자.