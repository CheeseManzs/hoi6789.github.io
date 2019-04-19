import json
import random
from random import randint
js = open('idle.js', 'r')

# dynamically generate javascript code
def output(x):
  global js
  javascript_out = "var pythonevent = JSON.parse('{}');".format(json.dumps(x))
  javascript_out += js.read()
def generate():
  possevent = ['You lose half your wood', 'You lose half your stone']
  ifevent = randint(1, 10)
  if possevent == 10:
    event = random.choice(possevent)
    output(event)
  if possevent > 10:
    event = 'nothing of importance happened today...'
    output(event)
