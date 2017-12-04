from urllib.request import FancyURLopener

url = "http://www.seriouseats.com/2015/02/how-to-make-chinese-hot-pot-at-home-guide.html"

class AppURLopener(FancyURLopener):
    version = "Mozilla/5.0"

opener = AppURLopener()
response = opener.open(url)

data = response.read()
text = data.decode("utf-8")
print(text)
