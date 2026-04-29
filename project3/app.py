import os
from flask import Flask, render_template, request
from mbta_helper import find_stop_near

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/result", methods=["POST"])
def result():
    place_name = request.form["place_name"]

    try:
        stop_info = find_stop_near(place_name)

        if stop_info is None:
            return render_template(
                "result.html",
                place_name=place_name,
                error="Could not find a nearby MBTA stop."
            )

        stop_name, wheelchair_status, user_lat, user_lon, stop_lat, stop_lon = stop_info

        return render_template(
            "result.html",
            place_name=place_name,
            stop_name=stop_name,
            wheelchair_status=wheelchair_status,
            user_lat=user_lat,
            user_lon=user_lon,
            stop_lat=stop_lat,
            stop_lon=stop_lon,
            mapbox_token=os.getenv("MAPBOX_API_KEY"),
            error=None
        )

    except:
        return render_template(
            "result.html",
            place_name=place_name,
            error="Something went wrong. Please try another location."
        )

if __name__ == "__main__":
    app.run(debug=True)