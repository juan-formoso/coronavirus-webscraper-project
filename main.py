import requests
import json

API_KEY = "tqT3LV5LTVBd"
PROJECT_TOKEN = "t4YV1yd2o04o"
RUN_TOKEN = "tGKqm-Jp-rCm"

response = requests.get(f'https://www.parsehub.com/api/v2/projects/{PROJECT_TOKEN}/last_ready_run/data', params={"api_key": API_KEY})

data = json.loads(response.text)
