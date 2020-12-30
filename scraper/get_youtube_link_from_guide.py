import re
from bs4 import BeautifulSoup as soup


def getYoutubeLink(guide):
    start = re.escape("<iframe ")
    end = re.escape("frame")
    st = guide
    # result = re.sub("%s(.*)%s" % (start, end), "", st)
    video = re.search("%s(.*)%s" % (start, end), st)
    youtube_link = ""
    if video:
        video = re.search("%s(.*)%s" % (start, end), st).group(0)
        video = video.replace("data-src", "src")
        page_soup = soup(video, "html.parser")
        youtube_link = page_soup.find("iframe")["src"]
    return str(youtube_link)


def removeIframe(guide):
    start = re.escape("<iframe ")
    end = re.escape("iframe>")
    st = guide
    result = re.sub("%s(.*)%s" % (start, end), "", st)
    return result
