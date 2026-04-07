"""
Flask application for Chicago Crime Analysis.
"""
from flask import Flask, render_template

from .data import load_crime_data


def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__, template_folder="templates")

    crime_df = load_crime_data()
    app.config["CRIME_DF"] = crime_df

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/about")
    def about():
        return render_template("about.html")

    @app.route("/viz/placeholder")
    def viz_placeholder():
        return render_template("viz_placeholder.html")

    @app.route("/dashboards/time")
    def dashboard_time():
        return render_template(
            "dashboards/time.html",
            rows=len(app.config["CRIME_DF"]),
        )

    @app.route("/dashboards/space")
    def dashboard_space():
        return render_template(
            "dashboards/space.html",
            rows=len(app.config["CRIME_DF"]),
        )

    @app.route("/dashboards/types")
    def dashboard_types():
        return render_template(
            "dashboards/types.html",
            rows=len(app.config["CRIME_DF"]),
        )

    return app
