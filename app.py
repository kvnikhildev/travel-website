from flask import Flask, render_template

app = Flask(__name__)

destinations = [
    {"name": "Paris", "description": "The city of lights with Eiffel Tower.", "image": "https://example.com/paris.jpg"},
    {"name": "Tokyo", "description": "Modern city with traditional roots.", "image": "https://example.com/tokyo.jpg"},
    {"name": "New York", "description": "The Big Apple, a city that never sleeps.", "image": "https://example.com/ny.jpg"}
]

@app.route("/")
def index():
    return render_template("index.html", destinations=destinations)

@app.route("/destination/<name>")
def destination(name):
    dest = next((d for d in destinations if d["name"].lower() == name.lower()), None)
    if dest:
        return render_template("destination.html", destination=dest)
    return "Destination not found", 404

if __name__ == "__main__":
    app.run(debug=True)
