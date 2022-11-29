import pdb

from models.album import Album
from models.artist import Artist

import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

album_repository.delete_all()
artist_repository.delete_all()

artist_1 = Artist ("John Lennon")
artist_repository.create(artist_1)

artist_2 = Artist ("Paul McCartney")
artist_repository.create(artist_2)

album_1 = Album ("Milk and Honey", "Rock", artist_1)
album_repository.create(album_1)

album_2 = Album ("Band on the Run", "Rock", artist_2)
album_repository.create(album_2)

album_3 = Album ("Double Fantasy", "Rock", artist_1)
album_repository.create(album_1)

album_4 = Album ("McCartney", "Rock", artist_2)
album_repository.create(album_2)









pdb.set_trace()