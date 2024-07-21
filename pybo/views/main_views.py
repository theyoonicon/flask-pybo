from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix = '/')

@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/')
def index():
    return redirect(url_for('question._list'))

# url_for 함수에 전달된 question._list는 question, _list 순서로 해석되어 라우팅 함수를 찾는다.
# question은 등록된 블루프린트 별칭, _list는 블루프린트에 등록된 함수명이다. 
# 따라서 question._list는 question이라는 별칭으로 등록한 question_views.py 파일의 _list 함수를 의미한다. 
# 그리고 _list 함수에 등록된 URL 매핑 규칙은 @bp.route('/list/')이므로 url_for('question._list')는 
# bp의 프리픽스 URL인 /question/과 /list/가 더해진 /question/list/ URL을 반환한다.