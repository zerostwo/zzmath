from flask import Blueprint, render_template, redirect, request, flash, url_for
import hashlib
from flask import make_response
import xml.etree.ElementTree as ET

wechat = Blueprint(
      "wechat", __name__, template_folder="../templates", static_folder="../static")

WX_TOKEN = 'duansq'

@wechat.route("/wechat_api/", methods=['GET', 'POST'])
def index():
   if request.method == 'GET':
      token = WX_TOKEN
      data = request.args
      signature = data.get('signature', '')
      timestamp = data.get('timestamp', '')
      nonce = data.get('nonce', '')
      echostr = data.get('echostr', '')
      s = sorted([timestamp, nonce, token])
      # 字典排序
      s = ''.join(s)
      if hashlib.sha1(s.encode('utf-8')).hexdigest() == signature:
         # 判断请求来源，并对接受的请求转换为utf-8后进行sha1加密
         response = make_response(echostr)
         return response


def message_del(content): 
   # 次数是自定义的消息处理函数，自由发挥
   if "baidu" in content:
      message = "www.baidu.com"
   elif "金牛" in content:
      message = "贪财好色小心眼"
   else:
      message = "我不知道！"
   return message
