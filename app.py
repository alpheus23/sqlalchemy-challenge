import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

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

@app.route('/api/v1.0/precipitation')
def prcp():
    session = Session(engine)

    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    dates = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= prev_year).all()

    session.close()

    all_prcp = []
    for date, prcp in dates:
        prcp_dict = {}
        prcp_dict["date"] = date
        prcp_dict["prcp"] = prcp
        all_prcp.append(prcp_dict)

    return jsonify(all_prcp)


if __name__ == "__main__":
    app.run(debug=True)