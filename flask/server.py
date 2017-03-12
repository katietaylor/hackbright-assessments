from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


@app.route("/")
def index():
    """Show homepage."""

    return render_template("index.html")


@app.route("/application-form")
def application_form():
    """Show the application form"""

    job_positions = ["Software Engineer", "QA Engineer", "Product Manager"]

    return render_template("application-form.html", job_titles=job_positions)


@app.route("/application-success", methods=['POST'])
def application_success():
    """Show the application response."""

    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    job_title = request.form["job_title"]

    # add commas to the 1000's place and display 2 decimals places if needed.
    salary = request.form["salary"]
    if "." in salary:
        salary = "{:,.2f}".format(float(salary))
    else:
        salary = "{:,}".format(int(salary))

    return render_template("/application-response.html", first_name=first_name,
                           last_name=last_name, salary=salary,
                           job_title=job_title)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
