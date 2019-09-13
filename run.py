import argparse
import re
import sys
import requests

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
    data = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    return data.text

  @staticmethod
  def process(data):
    email_regex = re.compile('([A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4})', re.IGNORECASE)
    for email in email_regex.findall(data):
      yield email
      
def main():
  argparser = argparse.ArgumentParser()
  argparser.add_argument('--urls', dest='urls', required=True, help='Emails separated with comma.')
  
  parsed_args = argparser.parse_args()
  
  crawler = Crawler(parsed_args.urls)
  
  crawler.crawl()


if __name__ == "__main__":
    sys.exit(main())