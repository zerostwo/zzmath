from flask import Blueprint, render_template, redirect, request, flash, url_for

from app.models import User, ChangeLog, Feedback
import pandas as pd
import os
import time

zhihu = Blueprint(
    "zhihu", __name__, template_folder="../templates", static_folder="../static"
)
key_word_dict = {
    "chinese": "语文",
    "math": "数学",
    "english": "英语",
    "physics": "物理",
    "chemistry": "化学",
    "biology": "生物",
    "political": "政治",
    "history": "历史",
    "geography": "地理",
}

from psutil import *
from flask import jsonify
@zhihu.route("/hyakki/")
def hyakki():
   dict = {
      "memory": [virtual_memory().percent],
      "disk": [disk_usage("/").percent],
      "cpu": [cpu_percent(0)]
   }
   return jsonify(dict)


@zhihu.route("/")
def home():
    global key_word_dict
    result_df = pd.DataFrame(
        columns=["category", "category_zh", "columnsSum", "articlesSum"]
    )
    # 获取每个分类下的专栏数
    path = "app/static/data/zhihu"
    column = path + "/columns"
    date = max(os.listdir(column))
    i = 1
    for category in os.listdir(column + "/" + date + "/"):
        df = pd.read_excel(column + "/" + date + "/" + category)
        articles_sum = df["articlesCount"].sum()
        result_df.loc[i] = [
            category[:-5],
            key_word_dict[category[:-5]],
            len(df),
            articles_sum,
        ]
        i += 1
    columnsSums = result_df["columnsSum"].sum()
    articlesSums = result_df["articlesSum"].sum()
    rank = [i for i in range(1, len(result_df) + 1)]

    delta_df = pd.read_excel("app/static/data/zhihu/deltaChange/{date}.xlsx".format(date=date))

    delta_follower_top10 = delta_df.sort_values(by="deltaFollower", ascending=False)[:10]
    delta_follower_top10.index = range(1, len(delta_follower_top10) + 1)

    delta_voteup_top10 = delta_df.sort_values(by="deltaVoteupCount", ascending=False)[:10]
    delta_voteup_top10.index = range(1, len(delta_voteup_top10) + 1)

    delta_comment_top10 = delta_df.sort_values(by="deltaCommentCount", ascending=False)[:10]
    delta_comment_top10.index = range(1, len(delta_comment_top10) + 1)

    delta_rank = [i for i in range(1, len(delta_comment_top10) + 1)]
    result_df = result_df.to_dict()
    return render_template(
        "beagle/index.html",
        active="home",
        rank=rank,
        title="首页",
        result_df=result_df,
        delta_follower_top10=delta_follower_top10,
        delta_voteup_top10=delta_voteup_top10,
        delta_comment_top10=delta_comment_top10,
        delta_rank=delta_rank,
        columnsSums=columnsSums,
        articlesSums=articlesSums,
    )


@zhihu.route("/<category>")
def zhuanlan(category):
    global key_word_dict
    path = "app/static/data/zhihu/columns/"
    update_time = max(os.listdir(path))
    if os.path.exists(
            path
            + "{updateTime}/{category}.xlsx".format(
                updateTime=update_time, category=category
            )
    ):
        df = pd.read_excel(
            path
            + "{updateTime}/{category}.xlsx".format(
                updateTime=update_time, category=category
            ),
            index_col=0,
        )
    else:
        return render_template("beagle/pages-404.html"), 404

    rank = [i for i in range(1, len(df) + 1)]
    df = df.to_dict(orient="dict")
    return render_template(
        "beagle/column.html",
        rank=rank,
        updateTime=update_time.split("-"),
        category=category,
        title=key_word_dict[category],
        active=category,
        df=df,
    )


@zhihu.route("/<category>/<columnID>")
def article(category, columnID):
    global key_word_dict
    column_dir = ""
    path = "app/static/data/zhihu/articles/"
    update_time = max(os.listdir(path))
    try:
        column_articles_dir = os.listdir(
            path + update_time + "/{category}".format(category=category)
        )
    except EOFError:
        return render_template("beagle/pages-404.html"), 404
    for i in column_articles_dir:
        if columnID == i[:-5]:
            column_dir = (
                    path + update_time + "/{category}/".format(category=category) + i
            )
    if os.path.exists(column_dir):
        df = pd.read_excel(column_dir, index_col=0)
    else:
        return render_template("beagle/pages-404.html"), 404
    df = df.sort_values(by="articleUpdatedTime", ascending=False)
    rank = [i for i in range(1, len(df) + 1)]
    article_updated_time = []
    for i in range(1, len(df) + 1):
        article_updated_time.append(
            time.strftime("%Y/%m/%d", time.localtime(df.loc[i, "articleUpdatedTime"]))
        )
    path = "app/static/data/zhihu/columns/{updateTime}/{category}.xlsx".format(
        updateTime=update_time, category=category
    )
    columns = pd.read_excel(path, index_col=0)
    for i in range(len(columns)):
        if columnID == columns.iloc[i, 1].split("/")[-1]:
            column_name = columns.iloc[i, 0]
            column_url = columns.iloc[i, 1]
            author_name = columns.iloc[i, 2]
            author_url = columns.iloc[i, 3]
    df = df.to_dict()
    return render_template(
        "beagle/article.html",
        rank=rank,
        columnName=column_name,
        columnUrl=column_url,
        title=column_name,
        category=key_word_dict[category],
        active=category,
        df=df,
        authorName=author_name,
        authorUrl=author_url,
        article_updated_time=article_updated_time,
    )


@zhihu.route("/feedback", methods=["GET", "POST"])
def feedback():
    #descriptions = Feedback
    feedbacks = Feedback.query.order_by(Feedback.id.desc())
    #print(feedbacks)
    if request.method == "POST":
        description = request.form.get("description")
        contact_details = request.form.get("contact_details")
        f = Feedback()
        f.description = description
        f.contact_details = contact_details
        f.save()
        print(description, contact_details)
        flash("反馈提交成功，我们将会尽快处理!")
        return redirect(url_for('zhihu.home'))
    return render_template("beagle/feedback.html", title="反馈", feedbacks=feedbacks, f = "feedback")

@zhihu.route("/documentation")
def documentation():
    return render_template("beagle/documentation.html", docs="docs", title="文档")
