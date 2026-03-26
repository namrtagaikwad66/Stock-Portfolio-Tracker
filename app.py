from flask import Flask, render_template, request
from tracker import calculate_portfolio

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = {}
    total = 0

    if request.method == "POST":
        symbol = request.form["stock"].upper()
        qty = int(request.form["quantity"])

        portfolio = {symbol: qty}
        total, result = calculate_portfolio(portfolio)

    return render_template("index.html", result=result, total=total)


if __name__ == "__main__":
    app.run(debug=True)