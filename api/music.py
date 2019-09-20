
import json
from base import FanartBase
from models.artist import Artist
from models.albums import Albums



class Music(FanartBase):

    def __init__(self):
        """ API for Music related functions
            Reference: https://fanarttv.docs.apiary.io/#reference/music
        """
        super(Music, self).__init__()

        # Set the API for /music
        self.http.set_base('/music')

    def artist(self, mbid_id):
        """ Query for artist
            mbid_id | (string) of MusicBrain's ID
        """
        self.http.set_base('/music')

        response = self.http.get(mbid_id)
        response = json.loads(response.text)

        artist = Artist()
        artist.load(response)
        return artist

    def album(self, album_mbid_id):
        # Set the API for /music
        self.http.set_base('/music/albums')
        
        response = self.http.get(album_mbid_id)
        response = json.loads(response.text)

        albums = Albums()
        albums.load(response)

        return albums


