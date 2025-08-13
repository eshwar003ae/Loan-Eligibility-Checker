from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Get form data
    name = request.form['name']
    gender = request.form['gender']
    monthly_income = float(request.form['monthly_income'])
    annual_income = float(request.form['annual_income'])
    loan_amount = float(request.form['loan_amount'])
    property_worth = float(request.form['property_worth'])
    credit_score = int(request.form['credit_score'])

    # Calculate loan eligibility
    total_worth = annual_income + property_worth
    loan_limit = total_worth * 0.4  # 40% of total worth

    if loan_amount <= loan_limit and credit_score >= 650:
        prediction = f"Loan Approved ✅. Your eligible loan limit is ₹{loan_limit:,.0f}"
        reason = ""
    else:
        prediction = "Loan Rejected ❌"
        if credit_score < 650:
            reason = "Low credit score"
        elif loan_amount > loan_limit:
            reason = f"Loan amount exceeds 40% limit (Max allowed: ₹{loan_limit:,.0f})"
        else:
            reason = "Not eligible as per policy"

    return render_template("result.html", prediction=prediction, reason=reason)

if __name__ == "__main__":
    app.run(debug=True)
