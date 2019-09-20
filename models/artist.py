
class ArtistBase(object):
    def __init__(self, dict_key):
        """
        dict_key | (string) from the API response to load the data to
        """
        self.all = []
        self.key = dict_key

    def load(self, response):
        """ Load data from a certain key """
        self.all = response.get(self.key, self.all)



class Artist(object):
    def __init__(self):
        self.name = ''
        self.mbid_id = ''
        self.hdmusiclogo = ArtistBase('hdmusiclogo')
        self.artistbackground = ArtistBase('artistbackground')
        self.artistthumb = ArtistBase('artistthumb')
        self.musicbanner = ArtistBase('musicbanner')
        self.musiclogo   = ArtistBase('musiclogo')

    def load(self, response):
        """ Receiving HTTP response, load whatevern we need here """
        self.name = response.get('name', '')
        self.mbid_id = response.get('mbid_id', '')

        self.hdmusiclogo.load(response)
        self.artistthumb.load(response)
        self.musicbanner.load(response)
        self.musiclogo.load(response)
        self.artistbackground.load(response)

    def __repr__(self):
        return """<Artist %s, 
                    hdmusiclogo(%s)
                    artistbackground(%s)
                    artistthumb(%s)
                    musicbanner(%s)
                    musiclogo(%s)""" % (self.name, 
                                    len(self.hdmusiclogo.all),
                                    len(self.artistbackground.all),
                                    len(self.artistthumb.all),
                                    len(self.musicbanner.all),
                                    len(self.musiclogo.all))