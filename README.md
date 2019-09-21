# FanArt API
FanArt.tv API implementation for Python2.x based on: https://fanarttv.docs.apiary.io/

# Usage - Music
FanArt console: https://fanarttv.docs.apiary.io/#reference/music/get-album?console=1

Review the test file: `test_music` for a working sample
```
from api.music import Music

m = Music()
m.set_api_key('Your personal API key for FanArt')
```

### music/artist
```
# artist API
artist = m.artist(mbid_id)

# Access any attribute inside the artist 
# Summary will show all available attributes
print artist

# Access any attribute inside the artist by artist.X
backgrounds = artist.artistbackground
print backgrounds.all           # review what's inside
print backgrounds.getfirst()    # Most likes

# Access Artist's albums
albums = artist.get_albums()    # All
album = artist.albums.get_album('10c057fa-27a7-4122-a755-493c4c817603')     # Specific by MB ID ..
```

### music/albums
```
# Album
albums = m.album(mbid_id)

# Summary will show all available albums
print albums

# Since we requested only a single Album, only one will exists
album = albums.getfirst()

# Summary will show all available attributes
print album

# Access any attribute inside the album by album.X
print album.albumcover              # review what's insde
print album.albumcover.getfirst()   # Most likes
```

