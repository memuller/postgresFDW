import requests

class WikipediaSearch:

  def __init__(self, search, language='en'):
    self.search = search
    # https://en.wikipedia.org/w/api.php?action=opensearch&search=gender&limit=10&namespace=0&format=json
    url = 'https://%s.wikipedia.org/w/api.php?action=opensearch&search=%s&limit=%s&namespace=0&format=json' % (language, search, 10)
    
    response = requests.get(url)
    json = response.json()
    self.response = json
    
    self.items = []

    for i in range(len(json[1])):
      self.items.append({
        'title': json[1][i],
        'description': json[2][i],
        'url': json[3][i]
      })

  @staticmethod
  def query(search, language='en'):
    query = WikipediaSearch(search, language)
    return query.items