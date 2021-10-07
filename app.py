# flask 패키지에서 Flask 클래스를 임포트
import os

from flask import Flask

# 인스턴스 변수와 리터럴(생성자)
app = Flask(__name__)


# route경로로 접근 했을 때, 동작하는 함수
@app.route("/")
def hello():
    return "Hello World"
# @app.route("/test")
# def test():
#     return "Test page"


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=int(os.environ.get("PORT", 5000)))


