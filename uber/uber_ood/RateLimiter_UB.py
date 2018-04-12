/*
* Develop an API Rate-limit Throttling Client
* 要求写一个api， 请求第三方api， 如果一秒内的请求太多， 自己的api就直接忽略掉。
* 面试小哥给了个框架[此部分内容仅作者可见]
* 面试题目就这一个， 开始还有介绍自己和简历。 求水果啊。。

* 题目是RateLimit，允许每个客户在每秒内访问100次，bool isAllowed(int clientID)
* 我说那我用Token Bucket吧
* 但是写着写着他表示看不懂让我解释……
* 最后超了几分钟写完代码，没跑
* 感觉崩了more.

* 补充内容 (2018-2-1 13:33):
* 题目是RateLimit，允许每个客户在每秒内访问100次，bool isAllowed(int clientID)
* 我说那我用Token Bucket吧
* 这是回复可见里面的内容……

* R2 美国朋克妹，面试邮件会发面试的人。 上来一顿聊。还比较好沟通。 然后是经典题。ip rateLimitCall. 题目就一句话，然后全是自己设计，
* 题目其实 没有定义，就要自己设计各种入口包装什么的。好像题目也是自己理解。。。不知道写的可不可以，反正就用queue 做的。

* 题目是rate limiter，1 sec里不能超过100次request。一开始脑子有点懵，后来小哥哥提示了一些才终于想通。。
**/
import datetime
import time
class GoogleMapsClient(object):
    """3rd party maps client; we CANT EDIT THIS."""

    def __init__(self):
        self.requests_made = 0.

    def make_request(self):
        self.requests_made += 1
        now = datetime.datetime.now().time().
        return "%d - %s - San Francisco" % (self.requests_made, now)

class RequestMaker(object):
    def __init__(self, max_request_number):
        self.queue = []
        self.max_request_number = max_request_number

    def make_request(self):
        self.request_time = datetime.datetime.now()
        self.check_limit()
        if len(self.queue) < self.max_request_number:
            self.queue.append(self.request_time)
            GoogleMapsClient.make_request()

    def check_limit(self):
        while self.queue:
            if self.request_time - self.queue[0] > datetime.timedelta(seconds=1):
                self.queue.pop(0)
            else:
                break
GoogleMapsClient()
