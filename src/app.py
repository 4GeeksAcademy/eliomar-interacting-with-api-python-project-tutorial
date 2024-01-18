import os
from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()

client_id = os.environ.get("473ab671b245469fa98250d34ce26723")
client_secret = os.environ.get("7d35bd5f67714510ae40944dc2261104")

import spotipy
spotipy.Spotify()

# 1) Connect to the database here using the SQLAlchemy's create_engine function

# 2) Execute the SQL sentences to create your tables using the SQLAlchemy's execute function

# 3) Execute the SQL sentences to insert your data using the SQLAlchemy's execute function

# 4) Use pandas to print one of the tables as dataframes using read_sql function