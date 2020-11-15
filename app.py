from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return (
        f"Welcome to my API!<br/>"
        f"Available Routes: <br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start>"
    )

if __name__ == "__main__":
    app.run(debug=True)