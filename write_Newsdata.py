import sqlite3
import json
import glob
from datetime import datetime

con = sqlite3.connect("D:/django_restful_api/mysite/db.sqlite3")

news_data_path = "news_data/wealth/*/*/*.json"
data_paths = glob.glob(news_data_path)
for path in data_paths:
    with open(path, 'r', encoding='utf-8-sig') as jf:
        d = json.load(jf)
        for article in d:
            title = article['title']
            author = article['author']
            date_time = article['date_time']
            date_time = datetime.strptime(date_time,"%Y/%m/%d").strftime("%Y-%m-%d")
            link = article['link']
            label = article['label']
            website = article['website']
            content = article['content']
            keyword = article['keyword']
            
            cursorObj = con.cursor()
            cursorObj.execute("""INSERT INTO api_newsarticle(title, author, date_time, link, label, website, content, keyword) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                (title, author, date_time, link, label, website, content, keyword))
            con.commit()