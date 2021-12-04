# Project Title: FirstPythonCrawler_HullDailyMail

# Project Description
Having played around with Python for a little while, I have decided to create a simple web crawler script that would scrape some data from a local news paper website, Hull Daily Mail. In short, the script was designed to load predefined website — Hull Daily Mail's front page — and scrape titles of all the articles found on that site, along with other information such as author/s name/s, article label, and the total count of the articles on website. Besides simple scraping, it also contains a function for counting various variables such as total number of articles, tags with most articles, tags with least articles. 

The data gathered using this code is stored in an .xlsx, and can be used for further analysis. In this case, I was not planning on using the data in any particular way, it was rather an experiement to see how quickly, and how easily I would have been able to develop such script. Therefore, the only analysis I conducted on the data were aimed at looking into which tags were most often used, on what dates, which authores published the most and least articles, and under which tags.

The script was designed to be run manually, however some degree of automation can be achieved by using Windows Scheduler, or creating a simple automation script in Python.
I am not an expert in programming, and a lot of the code was created by using resources found in various community groups, forums, etc. Majority of those have been appropiately referenced within the code.

# Main Functions

- Using BeatifulSoup to scrape data from Hull Daily Mail's front page: articles' titles, articles' labels, articles' authors;
- Count the number of articles per each tag/ author/ date;
- Display simple summary information about the progress of scraping, and the data gathered;
- Store the gathered data in .xlsx format;

# Future improvements

- 
-
-

# License
If you find any part of this code useful, feel free to reuse it, modify it, and otherwise change it in any way you want.
Author attribution is always appreciated, and so are the feedback and comments on potential improvements.
