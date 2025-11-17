from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# ---------- LOGIN PAGE ----------
@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Note: In a real app, you must validate credentials here.
        return redirect("/index")
    return render_template("login.html")

# ---------- REPORT FORM PAGE ----------
@app.route("/index", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get form data
        name = request.form.get("name")
        email = request.form.get("email")
        crimeType = request.form.get("crimeType")
        location = request.form.get("location")
        description = request.form.get("description")

        # Save to SQLite
        try:
            con = sqlite3.connect("crime_portal.db")
            cur = con.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS reports (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    email TEXT,
                    crimeType TEXT,
                    location TEXT,
                    description TEXT
                )
            """)
            cur.execute(
                "INSERT INTO reports (name, email, crimeType, location, description) VALUES (?, ?, ?, ?, ?)",
                (name, email, crimeType, location, description)
            )
            con.commit()
            con.close()
            
            # 1. Use Post/Redirect/Get (PRG) pattern: Redirect back to /index
            #    and pass a status flag in the query string.
            return redirect("/index?status=success")

        except Exception as e:
            print(f"Database Error: {e}")
            # Redirect with an error flag
            return redirect("/index?status=error")

    # 2. Get the status flag from the URL query parameters (e.g., ?status=success)
    submission_status = request.args.get('status')
    
    # Pass the status to the template
    return render_template("index.html", status=submission_status)

# ---------- SUCCESS PAGE (Still commented out) ----------
#@app.route("/success")
#def success():
 #   return render_template("success.html")

# ---------- RUN APP ----------
if __name__ == "__main__":
    app.run(debug=True)