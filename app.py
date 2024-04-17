from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "I am almost a DevOps Engineer!"

if __name__ == "__main__":
    # Run the Flask app on host 0.0.0.0 and port 5000
    app.run(use_reloader=True, host='0.0.0.0', port=5000)
