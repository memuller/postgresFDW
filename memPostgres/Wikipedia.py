from multicorn import ForeignDataWrapper
from multicorn.utils import *
from models import WikipediaSearch

import re, string
re.UNICODE = True

class Wikipedia(ForeignDataWrapper):
  def __init__(self, options, columns):
    # options: dict
    # columns: [ column_name: type ]
    super(Wikipedia, self).__init__(options, columns)
    self.columns = columns
    if 'language' in options:
      self.language = options['language']
    else:
      self.language = 'en'   
  
  def execute(self, quals, columns):
    query = None
    if len(quals) == 0:
      raise Exception('At least one WHERE by title is requiredaa')
    for qual in quals:
      if qual.field_name != 'title':
        raise Exception('Only searches by title are supported')
      if qual.operator == '=':
        query = qual.value
      if qual.operator in ['~', '~*', '~~']:
        query = re.sub('[~^$\/%*]', '', qual.value)
    if not query:
      raise Exception("At least one WHERE by title is requiredaaa")
          
    search = WikipediaSearch(query, self.language)
    return search.items
