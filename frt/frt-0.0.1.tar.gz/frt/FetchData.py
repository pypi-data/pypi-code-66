import pandas as pd
import numpy as np
import datetime as dt
import wrds

###################
# Connect to WRDS #
###################
conn = wrds.Connection(wrds_username="jeanpaulvanbrak")
# username: jeanpaulvanbrak
# password: vJ9X*l4!Q46&

# List all libraries in wrds
conn.list_libraries()

# List all tables in the "crsp" library
conn.list_tables(library='crsp')

# Describe the "monthly stock file" table
conn.describe_table(library='crsp', table='msf')

# Get the first x rows of a table
conn.get_table(library='crsp', table='msf', obs=5)

