from flask import Flask, request, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def own():
    return render_template('index.html')

@app.route("/ownpage", methods=["GET", "POST"])
def mypage():
    if request.method == "POST":
        name = request.form["name"]
        bday = request.form["bday"]  
        
        birth_date = datetime.strptime(bday, "%Y-%m-%d")

        today = datetime.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

        return jsonify({"name": name, "age": age})
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)