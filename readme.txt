Dilbert scraper!
A friend of mine asked to show him how one can use Scrapy (http://scrapy.org) to extract some
data from a website (to be more specific - how to download files). For demonstration purposes
I wrote for him this very basic scraper/images downloader.
As I'm a huge Dilbert fan (http://www.dilbert.com/) all this code does is scrapping all of the
Dilbert strips from now back to 2010 and puts them into the ./dilbert-strips/ folder.

To run the scraper enter the project directory and type:
    scrapy crawl dilbert
Then watch how ./dilbert-strips/ is being filled with files.

