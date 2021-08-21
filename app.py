# Import dependencies
from flask import Flask
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# Set up database
engine = create_engine('sqlite:///hawaii.sqlite')
Base = automap_base()
Base.prepare(engine, reflect=True)

# Create variables
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create session link
sesion = Session(engine)

# Create instance
app = Flask(__name__)

# Create routes