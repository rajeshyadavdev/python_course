""" 
ChainMap combines multiple dictionaries into one view.

Synatx:
  from collections import ChainMap
  chain_name = ChainMap(dict1, dict2, dict3)
  
1. ChainMap groups multiple dictionaries together.  
2. It does not merge them permanently.
3. It creates a combined view.
4. When searching for a key, Python checks dictionaries from left to right.
5. If the same key exists in multiple dictionaries, the first one is used.  
"""

from collections import ChainMap
defaults = {
"theme": "light",
"language": "English"
}
user_settings = {
"theme": "dark"
}
settings = ChainMap(user_settings, defaults)
print(settings["theme"])      # dark
print(settings["language"])   # Engish

''' 
Explanation
  1. "theme" exists in user_settings, so "dark" is used.
  2. "language" is not in user_settings, so Python checks defaults.

'''
# Useful ChainMap Features
''' 
Feature           Meaning                                 Example
maps              Shows all dictionaries                  settings.maps
new_child()       Adds new dictionary in front            settings.new_child({...})
parents           Removes first dictionary from view      settings.parents'''