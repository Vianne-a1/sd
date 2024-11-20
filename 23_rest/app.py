## Team topher API
## Tyang Brudinski
# Nov 19 2024
# rest APIs

# Lm0DcjX5IF9ojaCo88NHCv4m5qSUxPGnPd1L5bb2


from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
import requests
import json

def main():
    response = requests.get("https://api.nasa.gov/planetary/apod?api_key=Lm0DcjX5IF9ojaCo88NHCv4m5qSUxPGnPd1L5bb2")
    printf(response.status_code)
    printf(response.json())
    printf("hi")
