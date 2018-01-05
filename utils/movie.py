from __future__ import absolute_import
from __future__ import print_function

import os
import sys
import json
import requests

from utils.api.tmdb import TMDB
from utils.api.douban import Douban

class API:
    def __init__(self):
        self.tmdb = TMDB()
        self.douban = Douban()

class Movie:
    def __init__(self):
        self.api = API()

    def search(self, **kwargs):
         tmdb_id = self.api.tmdb.search(query = kwargs['query'])
         imdb_id = self.api.tmdb.get(movie_id = tmdb_id)
         return imdb_id

    def get(self, **kwargs):
        return self.api.douban.imdb(imdb_id = kwargs['imdb_id'])

# rename
movie = Movie()