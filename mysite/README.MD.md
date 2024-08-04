---
title: news article api view

---

# news article api view
## Demo Restful api by Django framework
1. 所有新聞文章內容
### API接口 http://127.0.0.1:8000/newsarticles
### 這個api傳回所有新聞文章的內容。每篇文章包含標題、發佈時間、作者、連結等資訊。
![image](https://hackmd.io/_uploads/BJ9vM02tC.png)

2. 每篇文章內容 http://127.0.0.1:8000/article/4
### ![image](https://hackmd.io/_uploads/SyupM0hYA.png)
### 這個api傳回特定文章詳細內容。透過提供文章的ID，可以獲得該文章的完整訊息。

3. Html呈現新聞文章內容 http://127.0.0.1:8000/news_list
### ![image](https://hackmd.io/_uploads/rkdW7CnK0.png)
### 這個頁面以 HTML 格式顯示所有新聞文章的清單。使用者可以直接在網頁上查看文章標題和發布日期，並點擊連結查看每篇文章的詳細內容

