from flask import Flask

app = Flask(__name__)

CHANNELS = {
  'qazi': 'UCqrILQNl5Ed9Dz6CGMyvMTQ',
  'mrbeast': 'UCX6OQ3DkcsbYNE6H8uQQuVA',
  'mkbhd': 'UCBJycsmduvYEL83R_U4JriQ',
  'pm': 'UC3DkFux8Iv-aYnTRWzwaiBA',
}

@app.route('/')
def index():
  return 'HOME PAGE'
  
app.run(host='0.0.0.0', port=81)