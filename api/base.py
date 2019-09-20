import requests


class FanartHTTPNoAPIKeyFound(Exception):
    def __init__(self):
        self.value = 'API Key was not found. in order to make HTTP calls, you must set_api_key()'

    def __str__(self):
        return repr(self.value)

class FanartHTTP(object):
    """ Handle all HTTP requests """

    def __init__(self):
        self.host = 'http://webservice.fanart.tv'
        self.api_version = 'v3'
        self.base = '/',
        self.api_key = ''

    def set_base(self, base):
        self.base = base

    def run(self, method, endpoint, params=None):
        if not self.api_key:
            # Can't make HTTP w/o API key
            raise FanartHTTPNoAPIKeyFound

        url = "{host}/{version}{base}/{endpoint}?api_key={key}".format(
                host=self.host,
                version=self.api_version,
                base=self.base,
                endpoint=endpoint,
                key=self.api_key)

        print "URL:", url
        return requests.request(method, url, data=params)

    def get(self, url):
        return self.run('GET', url)


class FanartBase(object):

    def __init__(self):
        self.http = FanartHTTP()

    def set_api_key(self, key):
        """ Set another key, other than default """
        self.http.api_key = key

