import os
import webbrowser


chrome_path = "open -a /Applications/Google\ Chrome.app %s"

class Video():
    def __init__(self, title, duration):


class Movie(Video):
    """This class provides a way to store movie related information."""

    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
    # Open browser and play trailer
        webbrowser.get(chrome_path).open(self.trailer_youtube_url)


class TvShow(Video):
    def __init__(self, senson, episode, tv_station):


    def get_list(self):