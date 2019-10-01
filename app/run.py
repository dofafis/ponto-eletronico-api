from app import create_app
import sys

config = sys.argv[1]
app = create_app(config)
app.run()