

class AlbumAttribute(object):
    def __init__(self, dict_key):
        self.key = dict_key
        self.all = []

    def load(self, response):
        self.all = response.get(self.key, [])

    def getfirst(self):
        """ Get object with most likes """
        if not self.all:
            return

        return self.all[0]

class Album(object):

    def __init__(self, mbid_id=None):
        """
        mbid_id | (string) MusicBrainz album id
        """
        self.mbid_id = mbid_id
        self.albumcover = AlbumAttribute('albumcover')
        self.cdart = AlbumAttribute('cdart')

    def load(self, response):
        self.mbid_id = response.get('mbid_id', '')

        self.albumcover.load(response)
        self.cdart.load(response)

    def __repr__(self):
        return """<Album %s
        albumcover(%s)
        cdart(%s)\n""" % (self.mbid_id, 
                        len(self.albumcover.all), 
                        len(self.cdart.all))

class Albums(object):
    def __init__(self):
        # Artist details
        self.name = ''
        self.mbid_id = ''

        # Albums specific
        self.sorted_ids = []
        self.all = {}

    def load(self, response):
        self.mbid_id = response.get('mbid_id', '')
        self.name    = response.get('name', '')

        # Load Albums
        self.sorted_ids = response.get('albums', {}).keys()
        _albums = response.get('albums', {})
        for mbid_id in _albums.keys():
            collected_album = Album(mbid_id)
            collected_album.load(_albums[mbid_id])

            self.all[mbid_id] = collected_album

    def getfirst(self):
        """ Return the albums with the most likes """
        if not self.sorted_ids:
            return

        first_id = self.sorted_ids[0]
        return self.all.get(first_id)

    def get_albums(self):
        """ Return all available albums """
        return self.all

    def get_album(self, mbid_id):
        """ Get album by its MB ID """
        return self.all.get(mbid_id)

    def __repr__(self):
        return """<Albums mbid_id(%s) all(%s)""" % (self.mbid_id, len(self.all))

