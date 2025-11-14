from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    email = request.form["email"]
    crime_type = request.form["crimeType"]
    location = request.form["location"]
    description = request.form["description"]

    print("\n----- New Crime Report -----")
    print("Name:", name)
    print("Email:", email)
    print("Crime Type:", crime_type)
    print("Location:", location)
    print("Description:", description)
    print("-----------------------------\n")

    return "Report submitted successfully!"

if __name__ == "__main__":
    app.run(debug=True)
