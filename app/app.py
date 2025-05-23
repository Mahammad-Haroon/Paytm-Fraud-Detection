from flask import Flask, request, render_template, redirect, url_for, session
import joblib
import numpy as np

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Required for session management

# Load trained model
model = joblib.load("C:\\Users\\haroo\\OneDrive\\Desktop\\client 3\\fraud_detection_model.pkl")

# Login route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        if email == "paytm@gmail.com" and password == "paytm@123":
            session["logged_in"] = True
            return redirect(url_for("index"))  # Redirect to index.html after login
        else:
            return render_template("login.html", error="Invalid email or password")
    return render_template("login.html")

# Logout route
@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    return redirect(url_for("login"))

# About Us route
@app.route("/about")
def about():
    return render_template("about.html")

# Dashboard route (protected)
@app.route("/dashboard")
def dashboard():
    if not session.get("logged_in"):
        return redirect(url_for("login"))  # Redirect to login if not logged in
    return render_template("dashbord.html")

# Home route (redirect to login)
@app.route("/")
def home():
    return redirect(url_for("login"))

# Index route (protected)
@app.route("/index")
def index():
    if not session.get("logged_in"):
        return redirect(url_for("login"))  # Redirect to login if not logged in
    return render_template("index.html")

# Predict route (protected)
@app.route("/predict", methods=["POST"])
def predict():
    if not session.get("logged_in"):
        return redirect(url_for("login"))
    try:
        # Extract form data
        step = float(request.form["step"])
        amount = float(request.form["amount"])
        oldbalanceOrg = float(request.form["oldbalanceOrg"])
        newbalanceOrig = float(request.form["newbalanceOrig"])
        oldbalanceDest = float(request.form["oldbalanceDest"])
        newbalanceDest = float(request.form["newbalanceDest"])
        transaction_type = request.form["type"]

        # One-hot encoding for transaction type
        type_encoded = [0, 0, 0, 0]  # [CASH_OUT, DEBIT, PAYMENT, TRANSFER]
        type_mapping = {"CASH_OUT": 0, "DEBIT": 1, "PAYMENT": 2, "TRANSFER": 3}
        if transaction_type in type_mapping:
            type_encoded[type_mapping[transaction_type]] = 1

        # Prepare input data
        input_data = np.array([[step, amount, oldbalanceOrg, newbalanceOrig, oldbalanceDest, newbalanceDest] + type_encoded])

        # Predict fraud
        prediction = model.predict(input_data)[0]
        result = "Fraudulent Transaction" if prediction == 1 else "Legitimate Transaction"

        return render_template("result.html", prediction_text=result)
    except Exception as e:
        return render_template("result.html", prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)