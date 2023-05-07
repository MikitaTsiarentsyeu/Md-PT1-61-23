#Write a decorator function that caches the return value of a function with a dictionary. 
#If the function is called again with the same arguments, return the cached value instead of computing it again.

import json

def cash_decor(func):
  cash_dict = {}
  def wrapper(*args, **kwargs):
    key = json.dumps(args) + json.dumps(kwargs)
    if key in cash_dict:
      return cash_dict[key]
    else:
      res = func(*args, **kwargs)
      cash_dict[key] = res
      return res
  return wrapper


