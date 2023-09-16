import requests
from requests.models import Response


INVALID_CHARACTERS = "'/.!"


class AZLyrics():
    """
    Scrape song's lyrics from:

        https://www.azlyrics.com

    """
    def __init__(self, artist: str, song: str):
        self._artist = artist
        self._song = song

    def _parse_artist(self) -> str:
        """
        url' syntax requires artist name to be:
            - no spaces
            - all lower case
        """
        return self._artist.lower().replace(" ", "")

    def _parse_song(self) -> str:
        """
        url' syntax requires song name to be:
            - no spaces
            - all lower case
            - without invalid characters
        """
        out = self._song.lower().replace(" ", "")
        for c in INVALID_CHARACTERS:
            out = out.replace(c, "")
        return out

    def scrape(self) -> Response:
        """
        Retrives url's content
        """

        URL = self.url()

        response = requests.get(URL)

        return response

    def url(self) -> str:
        url_syntax = "https://www.azlyrics.com/lyrics/{}/{}.html"
        return url_syntax.format(self._parse_artist(), self._parse_song())
