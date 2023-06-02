from flask import Flask

app = Flask(__name__)
#hello this is a test
@app.route("/")
def hello():
    return "Hello, this is for CICD only"
if __name__ == "__main__":
    app.run()