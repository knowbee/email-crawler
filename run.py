import argparse
import re
import sys
from urllib.request import urlopen

class Crawler(object):
  
  def __init__(self, urls):
    self.urls = urls.split(',')
  
  def crawl(self):
    for url in self.urls:
      data = self.request(url)
      for email in self.process(data):
        print(email)
      
  
  @staticmethod
  def request(url):
    
    response = urlopen(url)
    return response.read().decode('utf-8')

  @staticmethod
  def process(data):
    for email in re.findall(r'(\w+@\w+\.com)', data):
      yield email
      
  
  
def main():
  argparser = argparse.ArgumentParser()
  argparser.add_argument('--urls', dest='urls', required=True, help='Emails separated with comma.')
  
  parsed_args = argparser.parse_args()
  
  crawler = Crawler(parsed_args.urls)
  
  crawler.crawl()


if __name__ == "__main__":
    sys.exit(main())