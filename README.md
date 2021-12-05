# Project Title: FirstPythonCrawler_HullDailyMail

# Project Description
Having played around with Python for a little while, I have decided to create a simple web crawler script that would scrape some data from a local news paper website, Hull Daily Mail. In short, the script was designed to load predefined website — Hull Daily Mail's front page — and scrape titles of all the articles found on that site, along with other information such as author/s name/s, article label, and the total count of the articles on website. Besides simple scraping, it also contains a function for counting various variables such as total number of articles, tags with most articles, tags with least articles. 

The data gathered using this code is stored in an .xlsx, and can be used for further analysis. In this case, I was not planning on using the data in any particular way, it was rather an experiement to see how quickly, and how easily I would have been able to develop such script. Therefore, the only analysis I conducted on the data were aimed at looking into which tags were most often used, on what dates, which authores published the most and least articles, and under which tags.

The script was designed to be run manually, however some degree of automation can be achieved by using Windows Scheduler, or creating a simple automation script in Python.
Also, I am not an expert in programming, and so a lot of the code was inspired by various solutions found on different community fora, wikis, etc. All the relevant sources are referenced in the code.

# Main Functions

- Using BeatifulSoup to scrape data from Hull Daily Mail's front page: articles' titles, articles' labels, articles' authors;
- Counting the number of articles per each tag/ author/ date;
- Displaying simple summary information about the progress of scraping, and the gathered data;
- Storing the gathered data in .xlsx file.

# Future improvements

- Adding more variables to scrape such as: Articles body text, articles' comments text, articles' comments number; One of the issues which prevented me from doing this in the first version of the script was a difficulty in obtaining information and guidance on the dynamic comments system used on their website. At the time of researching this, it seemed like an API was necessary to conduct   
- Analysing articles quality based on predefined criteria (Number of comments under articles as one of the measures of article popularity/ controvecy, scanning artciles body for gramatical and lexical mistakes, using corpus based system to define linguistic quality of the articles) by implementing different aspects computational linguistcs.
-

# License
If you find any part of this code useful, feel free to reuse it, modify it, and otherwise change it in any way you want.
Author attribution is always appreciated, and so are the comments, suggestions for improvements, and all other forms of feedback.
