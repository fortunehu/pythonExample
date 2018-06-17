#微信发消息
from __future__ import unicode_literals
from threading import Timer
from wxpy import *
import requests

bot = Bot()
#bot = Bot(console_qr=2, cache_path="botoo.pkl")

def get_news1():
     # 获取金山词霸每日一句，英文和翻译
    url = "http://open.iciba.com/dsapi/"
    r = requests.get(url)
    contents = r.json()['content']
    translation = r.json()['translation']
    return contents, translation

def send_news():
    try:
        #my_friends = bot.friends();
        my_friend = bot.friends().search(u'GreatWall')[0] #备注名
        my_friend.send(get_news1()[0])
        my_friend.send(get_news1()[1][5:])
        my_friend.send(u"来自ciba的心灵鸡汤！")
        print("send ok")
        #t = Timer(30,send_news)
        #t.start()
    except:
        #my_friends = bot.friends();
        print("send error")
        my_friend = bot.friends().search(u'GreatWall')[0] #备注名
        my_friend.send(u"今天消息发送失败了")


if __name__ == "__main__":
    send_news()
