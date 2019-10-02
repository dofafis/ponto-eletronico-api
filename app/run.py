from app import create_app
from db import db
import sys

config = sys.argv[1]
app, db = create_app(config)
app.run()