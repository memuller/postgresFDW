from multicorn import ForeignDataWrapper
import requests

class Test(ForeignDataWrapper):

  def __init__(self, options, columns):
    # options: dict
    # columns: [ column_name: type ]
    super(Test, self).__init__(options, columns)
    self.columns = columns
  
  def execute(self, quals, columns):
    # @ iteratable [ in order] || [ column_name: value ]
    for i in range(20):
      line = {}
      for column in self.columns:
        line[column] = '%s: %s' % (column, i)
      yield line
  