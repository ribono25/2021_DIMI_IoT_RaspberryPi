from flask import Flask, render_template

# Flask 객체 생성
# __name__은 파일명
app = Flask(__name__)


# 라우팅을 위한 뷰 함수 /파일명
@app.route("/")
def hello(): # 여러 줄 문자열 '''
    return render_template("hello.html", title="Hello, Flask")

@app.route("/first")
def first():
    return render_template("first.html")

@app.route("/second")
def second():
    return render_template("second.html")

# 터미널에서 직접 실행시킨 경우
if __name__ == "__main__":
    app.run(host="0.0.0.0")