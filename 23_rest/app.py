## Team topher API
## Tyang Brudinski
# Nov 19 2024
# rest APIs

# Lm0DcjX5IF9ojaCo88NHCv4m5qSUxPGnPd1L5bb2

from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Your NASA API key
API_KEY = "Lm0DcjX5IF9ojaCo88NHCv4m5qSUxPGnPd1L5bb2"


@app.route("/")
def home():
    try:
        # Fetch the Astronomy Picture of the Day (APOD) data
        response = requests.get(
            f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}")

        if response.status_code == 200:
            data = response.json()
            return render_template("index.html", apod_data=data)
        else:
            # Handle API errors gracefully
            return f"Error: Unable to fetch data from NASA API (Status Code: {response.status_code})"

    except requests.RequestException as e:
        # Handle connection errors
        return f"Error: {e}"


# Main entry point
if __name__ == "__main__":
    app.run(debug=True)
