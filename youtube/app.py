# Import jsonify
from flask import Flask, jsonify, render_template, url_for

# Import pprint to format data structure in console
import pprint

# Import requests library
import requests

# Create 'pretty-print' instance
pp = pprint.PrettyPrinter(indent=2)

app = Flask(__name__)

# Youtube channels
CHANNELS = {
  'cleverprogrammer': 'UCqrILQNl5Ed9Dz6CGMyvMTQ',
  'mrbeast': 'UCX6OQ3DkcsbYNE6H8uQQuVA',
  'mkbhd': 'UCBJycsmduvYEL83R_U4JriQ',
  'pm': 'UC3DkFux8Iv-aYnTRWzwaiBA',
}

@app.route('/')
def index():
  # Request API info
  url = "https://youtube138.p.rapidapi.com/channel/videos/"

  querystring = {"id": CHANNELS["cleverprogrammer"],"hl":"en","gl":"US"}

  headers = {
    "X-RapidAPI-Key": "aa2c2d1883mshe180f57453bf0a1p170092jsn98fe1fc8e5ca",
    "X-RapidAPI-Host": "youtube138.p.rapidapi.com"
  }

  response = requests.request("GET", url, headers=headers, params=querystring)

  # Convert response to json and save to data variable
  data = response.json()

  # Grab contents
  contents = data['contents']

  # Use list comprehension to get only videos if they have a publish time text
  videos = [video['video'] for video in contents if video['video']['publishedTimeText']]
  print(videos)

  # First video
  video = videos[0]
  
  # Return rendered index template w/ videos displayed
  return render_template('index.html', videos=videos, video=video)

# Local Machine
app.run(debug=True)