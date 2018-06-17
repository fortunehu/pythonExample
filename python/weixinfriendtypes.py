#微信获取用户类型
from __future__ import unicode_literals
from threading import Timer
from wxpy import *
import requests

bot = Bot()
#bot = Bot(console_qr=2, cache_path="botoo.pkl")
if __name__ == "__main__":
    male = female = other = 0
    my_friends = bot.friends()

    for iFriend in my_friends[1:]:
        sex0 = iFriend.sex
        if sex0 == 1:
            male += 1
        elif sex0 == 2:
            female += 1
        else:
            other += 1

    total = len(my_friends[1:])
    print(u"好友共有%d" % total)
    print(u"男性好友%d：%.2f%%" % (male,(float(male) / total * 100)))
    print(u"女性好友%d：%.2f%%" % (female,(float(female) / total * 100)))
    print(u"其他%d：%.2f%%" %(other,(float(other) / total * 100)))