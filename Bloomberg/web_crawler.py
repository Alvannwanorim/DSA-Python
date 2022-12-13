import collections


class HtmlParser:
    def __init__(self) -> None:
        self.parsed =[]
    def get_urls(self):
       """
       Return a list of urls
       """

class WebCrawler:
    def __init__(self) -> None:
        self.visited = set()
        self.queue = collections.deque()
        self.result = []
    
    def _get_domain_name(self, url):
        return url.split["http://"][1].split("/")[0]
    
    def crawl(self, startUrl):
        self.visited.add(startUrl)
        self.queue.append(startUrl)
        self.result.append(startUrl)

        parent_domain = self._get_domain_name(startUrl)

        while self.queue:
            for child in HtmlParser.get_urls(startUrl):

                if child not in self.visited and self._get_domain_name(child) ==parent_domain:

                    self.visited.add(child)
                    self.queue.append(child)
                    self.result.append(child)
        return self.result