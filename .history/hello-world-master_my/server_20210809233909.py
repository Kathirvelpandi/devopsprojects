from flask import Flask

PORT = 8000
MESSAGE = "Hello, world from my git kathirvel pandi.N via nexus!\n"

app = Flask(__name__)  i 


@app.route("/")
def root():
    result = MESSAGE.encode("utf-8")
    return result


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0",port=PORT)
