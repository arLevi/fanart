from albums import Albums


class ArtistAttribute(object):
    def __init__(self, dict_key):
        """
        dict_key | (string) from the API response to load the data to
        """
        self.all = []
        self.key = dict_key

    def load(self, response):
        """ Load data from a certain key """
        self.all = response.get(self.key, self.all)

    def __repr__(self):
        return """<Attribute key(%s) all(%s)""" % (self.key, len(self.all))


class Artist(object):
    def __init__(self):
        self.name = ''
        self.mbid_id = ''
        self.hdmusiclogo = ArtistAttribute('hdmusiclogo')
        self.artistthumb = ArtistAttribute('artistthumb')
        self.musicbanner = ArtistAttribute('musicbanner')
        self.musiclogo   = ArtistAttribute('musiclogo')
        self.artistbackground = ArtistAttribute('artistbackground')
        self.albums = Albums()

    def load(self, response):
        """ Receiving HTTP response, load whatevern we need here """
        self.name = response.get('name', '')
        self.mbid_id = response.get('mbid_id', '')

        self.hdmusiclogo.load(response)
        self.artistthumb.load(response)
        self.musicbanner.load(response)
        self.musiclogo.load(response)
        self.artistbackground.load(response)
        self.albums.load(response)

    def get_albums(self):
        """ Return all available albums """
        return self.albums

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
