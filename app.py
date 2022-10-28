from flask import Flask,jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/",methods=["GET"])
def home():

    response = jsonify(
        {
         "slackUsername": "jerryeagbesi", 
         "backend": True, 
         "age": 21, 
         "bio": "Hello I'm Jerry, I'm currently learning to become a world-class backend engineer 🤌"
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response,200




if __name__ == "__main__":
    app.run(debug=True)