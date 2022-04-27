#!/usr/bin/env python

import requests
import pandas as pd

urlc = "https://data.wa.gov/resource/mcr6-ujqw.csv"
#urlj = "https://data.wa.gov/resource/mcr6-ujqw.json"

impC = requests.get(urlc)
#impJ = requests.get(url).json()

df = pd.read_csv(impC)
print(len(df))
