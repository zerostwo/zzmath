from flask import Blueprint, render_template
from app.models import User
import pandas as pd
import os
import time

zhihu = Blueprint('zhihu', __name__, template_folder="../templates", static_folder="../static")


@zhihu.route('/')
def home():
    return render_template('base.html')


@zhihu.route('/<category>')
def index(category):
    key_word_dict = {
        "chinese": "语文",
        "math": "数学",
        "english": "英语",
        "physics": "物理",
        "chemistry": "化学",
        "biology": "生物",
        "political": "政治",
        "history": "历史",
        "geography": "地理"
    }
    rank = []
    column_names = []
    column_urls = []
    author_names = []
    author_urls = []
    followers = []
    articles_counts = []
    column_scores = []
    column_ids = []
    path = "app/static/data/zhihu/columns/"
    update_time = max(os.listdir(path))
    if os.path.exists(path + "{updateTime}/{category}.xlsx".format(updateTime=update_time, category=category)):
        df = pd.read_excel(path + "{updateTime}/{category}.xlsx".format(updateTime=update_time, category=category),
                           index_col=0)
    else:
        return render_template('error/404.html'), 404
    for i in range(1, len(df) + 1):
        column_ids.append(df.loc[i, "columnUrl"].split("/")[-1])
        rank.append(i)
        column_names.append(df.loc[i, "columnName"])
        column_urls.append(df.loc[i, "columnUrl"])
        author_names.append(df.loc[i, "authorName"])
        author_urls.append(df.loc[i, "authorUrl"])
        followers.append(format(df.loc[i, "followers"], '0,.0f'))
        articles_counts.append(df.loc[i, "articlesCount"])
        column_scores.append(format(round(df.loc[i, "columnScore"], 2), '0,.0f'))
    return render_template('zhihu/column.html',
                           rank=rank,
                           columnNames=column_names,
                           columnUrls=column_urls,
                           authorNames=author_names,
                           authorUrls=author_urls,
                           followers=followers,
                           articlesCounts=articles_counts,
                           columnScores=column_scores,
                           columnIDs=column_ids,
                           updateTime=update_time.split("-"),
                           category=category,
                           title=key_word_dict[category]
                           )


@zhihu.route('/<category>/<columnID>')
def zhuanlan(category, columnID):
    column_dir = ""
    path = "app/static/data/zhihu/articles/"
    update_time = max(os.listdir(path))
    column_articles_dir = os.listdir(path + update_time + "/{category}".format(category=category))
    for i in column_articles_dir:
        if columnID == i[:-5]:
            column_dir = path + update_time + "/{category}/".format(category=category) + i
    if os.path.exists(column_dir):
        df = pd.read_excel(column_dir, index_col=0)
    else:
        return render_template('error/404.html'), 404
    df = df.sort_values(by="articleUpdatedTime", ascending=False)
    rank = []
    article_title = []
    article_url = []
    article_author_name = []
    article_author_url = []
    article_voteup_count = []
    article_comment_count = []
    article_updated_time = []
    for i in range(1, len(df) + 1):
        rank.append(i - 1)
        article_title.append(df.loc[i, "articleTitle"])
        article_url.append(df.loc[i, "articleUrl"])
        article_author_name.append(df.loc[i, "articleAuthorName"])
        article_author_url.append(df.loc[i, "articleAuthorUrl"])
        article_voteup_count.append(df.loc[i, "articleVoteupCount"])
        article_comment_count.append(df.loc[i, "articleCommentCount"])
        article_updated_time.append(time.strftime("%Y/%m/%d", time.localtime(df.loc[i, "articleUpdatedTime"])))
    path = "app/static/data/zhihu/columns/{updateTime}/{category}.xlsx".format(
        updateTime=update_time, category=category)
    columns = pd.read_excel(path, index_col=0)
    for i in range(len(columns)):
        if columnID == columns.iloc[i, 1].split("/")[-1]:
            column_name = columns.iloc[i, 0]
            column_url = columns.iloc[i, 1]
            author_name = columns.iloc[i, 2]
            author_url = columns.iloc[i, 3]
    return render_template('zhihu/article.html',
                           rank=rank,
                           columnName=column_name,
                           columnUrl=column_url,
                           authorName=author_name,
                           authorUrl=author_url,
                           articleTitle=article_title,
                           articleUrl=article_url,
                           articleAuthorName=article_author_name,
                           articleAuthorUrl=article_author_url,
                           articleVoteupCount=article_voteup_count,
                           articleCommentCount=article_comment_count,
                           articleUpdatedTime=article_updated_time,
                           title=column_name)
