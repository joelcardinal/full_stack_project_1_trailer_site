# Python 2.7

import requests        # may require install: pip install requests
import unicodedata


class VideoData():
    '''Class with method to get JSON movie data from omdbapi.com'''

    def __init__(self, imdb_id):
        self.imdb_id = imdb_id

    def get_json_data(self, imdb_id):
        '''Queries omdbapi.com by IMDb ID to retreive video data

    Args:
        imdb_id (string): IMDb ID, found in movie URL (e.g. "tt2294629")

    Returns:
        dict: a dictionary translation of JSON data from request

        '''
        try:
            url_path = str("http://www.omdbapi.com/?i=") + str(
                self.imdb_id) + str(
                "&plot=short&r=json")
            response = requests.get(url_path)
            return response.json()
        except:
            print('Error requesting data.')
            return {'Response': 'False'}


class Movie(VideoData):
    '''Dynamically populates Movie instance attributes with movie data

    To conveniently access Movie instance attributes
    (e.g. Movie.plot) __init__ loops over json_data to dynamically
    create and populate attributes. *Starred attributes below not
    guaranteed.

    If data request is unsuccessful, Movie.response == 'False'


    Attributes:
        imdb_id (str): IMDb ID, found in movie URL (e.g. "tt2294629")
        youtube_trailer_url (str): YouTube URL of movie trailer
        json_data (dict): JSON response from omdbapi.com as dict, or ''
            if request unsuccessful
        *plot (str): Short summary of plot
        *rated (str): MPAA movie rating
        *response (str): 'True' if data response successful, else
            'False'
        *language (str): Comma separated list of languages available
        *title (str): Title of movie
        *country (str): Abreviation of country of origin
        *writer (str): Comma separated list of writers and role
        *metascore (str): Critic score from metacritic.com
        *imdbRating (str): Critic score from imdb.com
        *director (str): Comma separated list of directors
        *actors (str): Comma separated list of actors
        *year (str): Date released (e.g. "27 Nov 2013")
        *genre (str): Comma separated list of applicable genres
        *awards (str): Comma separated list and description of awards
        *runtime (str): Runtime of movie (e.g "102 min")
        *type (str): Constant "movie"
        *poster (str): URL to movie poster image
        *imdbVotes (str): Number of people who voted on IMDB rating
        *imdbID (str): IMDb ID, found in movie URL (e.g. "tt2294629")


    '''

    def __init__(self, imdb_id, youtube_trailer_url):
        VideoData.__init__(self, imdb_id)
        self.youtube_trailer_url = youtube_trailer_url
        self.json_data = self.get_json_data(imdb_id)
        for key, value in self.json_data.iteritems():
            # convert unicode to str
            ascii_value = unicodedata.normalize('NFKD',
                                                value).encode('ascii',
                                                              'ignore')
            setattr(self, key.lower(), ascii_value)
