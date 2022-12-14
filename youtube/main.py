# Import jsonify
from flask import Flask, jsonify, render_template, url_for

# Import pprint to format data structure in console
import pprint

# Import requests library
import requests

# Import numerize library
from numerize.numerize import numerize

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

# Active Channel
ACTIVE_CHANNEL = CHANNELS['cleverprogrammer']

# Data Structure
data = {
  'contents': [
    {
      type: 'video',
      'video': {
        'isLiveNow': False,
        'publishedTimeText': None, # Null in Python => None
        'stats': {
          'views': 23000
        },
        'title': 'Dummy Title 1',
        'thumbnails': [
          {
            'url': "link.com"
          }, 
          {
            'url': 'link.com'
          },
        ]
      }},
    {
      type: 'video',
      'video': {
        'isLiveNow': False,
        'publishedTimeText': '1 day ago' , # Null in Python => None
        'stats': {
          'views': 4500
        },
        'title': 'Dummy Title 2',
        'thumbnails': [
          {
            'url': "link.com"
          }, 
          {
            'url': 'link.com'
          },
        ]
      }},
  ],

  'cursorNext': 'test'
}

# Print data contents using 'pretty-print'
# pprint.pprint(data['contents'])

# Print first video in contents 
# first_video = data['contents'][0]['video']

# print(first_video)

# First video title
# print(first_video['title'])
# First video publish time
# print(first_video['publishedTimeText'])
# First video thumbnails
# print(first_video['thumbnails'])



@app.route('/')
def index():
  # Request API info
  url = "https://youtube138.p.rapidapi.com/channel/videos/"

  querystring = {"id": ACTIVE_CHANNEL,"hl":"en","gl":"US"}

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

# Create a template filter function that numerizes hig numbers => 4000 = 4k
@app.template_filter()
def numberize(views):
  return numerize(views, 1)

# Create a template filter that returns highest quality video [3] if at least 4 available else lowest quality [0]
@app.template_filter()
def highest_quality_img(thumbnails):
  return thumbnails[3]['url'] if len(thumbnails) >= 4 else thumbnails[0]['url']


# Replit config 
# app.run(host='0.0.0.0', port=81)

# Local Machine
app.run(debug=True)