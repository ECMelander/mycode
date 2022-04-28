#!/usr/bin/env python3

import wget

urlCSV = "https://data.wa.gov/resource/mcr6-ujqw.csv"
urlJSON = "https://data.wa.gov/resource/mcr6-ujqw.json"

wget.download(urlCSV, "/home/student/static/")
wget.download(urlJSON, "/home/student/static/")


