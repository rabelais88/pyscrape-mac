# pip install voluptuous
from voluptuous import Schema, Match

schema = Schema({
  'name': str,
  'price': Match(r'^[0-9,]+$'),
}, required=True)

schema({
  'name': 'grape',
  'price': '3,000'
})

# the codes below will cause error!
schema({
  'name': None,
  'price': '3!00'
})
