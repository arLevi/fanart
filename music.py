#!/usr/bin/env python

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


if __name__ == '__main__':
    m = Music()
    m.set_api_key('6b751c311d23f426e4524c78249cd62c')

    # Test: /music ( get artist with full query )
    if False:
        artist = m.artist('ea4dfa26-f633-4da6-a52a-f49ea4897b58')
        print "Artist object:", artist

    # Test: /music/albums
    if True:
        # W/o cdart
        albums = m.album('10c057fa-27a7-4122-a755-493c4c817603')
        print "Albums:", albums

        album = albums.getfirst()
        print "Album:", album
        if album:
            print "-> Cover:",  album.albumcover.getfirst()
            print "-> CD Art:", album.cdart.getfirst()


