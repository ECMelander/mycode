#!/usr/bin/env python

# make sure to install these packages before running:
# pip install pandas
# pip install sodapy

import pandas as pd
from sodapy import Socrata

# Unauthenticated client only works with public data sets. Note 'None'
# in place of application token, and no username or password:
client = Socrata("data.wa.gov", None)


# First 2000 results, returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get("mcr6-ujqw", limit=200000)

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)
print(type(results_df))
print(len(results_df))
print(results_df.columns)