from flask import Flask
#test edit
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello, this is for CICD only"
if __name__ == "__main__":
    app.run()