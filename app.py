from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/",methods=["GET"])
def home():
    return jsonify({
         "slackUsername": "jerryeagbesi", 
         "backend": True, 
         "age": 21, 
         "bio": "Hello I'm Jerry, I'm currently learning to become a world-class backend engineer 🤌"
    })




if __name__ == "__main__":
    app.run(debug=True)