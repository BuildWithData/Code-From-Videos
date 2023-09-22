from pytube import Channel
import requests

__doc__ = """

Scenario: I'd like to get the topX videos by views for a channel

Problem: pytube does not offer a fast way to do this,
         for example

        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        channel = Channel(channel_url)
        pairs = []
        for video in channel.videos:
            p = (video.watch_url,video.views)
            pairs.append(p)

        videos_sorted_by_view = sorted(pairs, key=lambda x: x[1], reverse=True)
        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        takes roughly 4/5 seconds per video

Workaround: get urls, then send a request and scrape number of views from the response

"""

############################################
# INPUT
url = "https://www.youtube.com/@MrBeast"

############################################
ch = Channel(url)

for v in ch.videos:

    url = v.watch_url
    print("VIDEO:", url)

    response = requests.get(url)

    if response.ok:
        response = response.text

        views = response.split("views")[-1][:50]

        # TODO: extract exact number from views
        # TODO: dump views to file or variable, then sort
        # TODO: send multiple requests at the same time
        #            https://scrapeops.io/python-web-scraping-playbook/python-requests-concurrent-threads/

        print("FOUND:", views)
