from pydiscourse import DiscourseClient
from bs4 import BeautifulSoup
from lexgpt import Lexgpt
import re
import time


HOST = 'HOST'
API_KEY = 'API_KEY'
USERNAME = 'Lexobot'


def htmlStripper(text: str):
    try:
        soup = BeautifulSoup(text, 'html.parser')
    except TypeError:
        return
    soup = soup.get_text()
    new_text = re.sub('@', '', soup)
    return new_text


def getNotifications(client: DiscourseClient):
    assert client._get('/notifications.json')['notifications'] != None
    return client._get('/notifications.json')['notifications']


def getTopicReplyNumber(client: DiscourseClient):
    return client._get('/notifications.json')['notifications'][0]['topic_id']


def getPostReplyNumber(client: DiscourseClient):
    return client._get('/notifications.json')['notifications'][0]['post_number']


def getUserReply(client: DiscourseClient):
    return client._get('/notifications.json')['']


def getReplyType(client: DiscourseClient):
    return client._get('/notifications.json')['notifications'][0]['notification_type']


def getPostReplyContent(client: DiscourseClient):
    notification: dict = client._get('/notifications.json')[
        'notifications'][0]
    try:
        post_number: int = int(notification['post_number'])
    except TypeError:
        return

    topic_id: int = notification['topic_id']

    return client.post(topic_id=topic_id, post_id=post_number)['post_stream']['posts'][len(client.post(topic_id=topic_id, post_id=post_number)['post_stream']['posts']) - 1]['cooked']


def markAsRead(client: DiscourseClient):
    return client._put('/notifications/mark-read.json')


class Lexobot:
    def __init__(self, host, api_key, username):
        self.host = host
        self.api_key = api_key
        self.username = username

    def __call__(self):

        client = DiscourseClient(
            host=self.host,
            api_username=self.username,
            api_key=self.api_key)

        print("Connected!")

        while True:
            if not getNotifications(client)[0]['read'] and getReplyType(client) != 5:
                if getPostReplyContent(client) == None: continue
                lexgpt = Lexgpt(htmlStripper(getPostReplyContent(client)))

                print(getReplyType(client=client))

                text = lexgpt().removeprefix(getPostReplyContent(client))

                client.create_post(text, getPostReplyNumber(client), getTopicReplyNumber(client))

                markAsRead(client)
                print("===Executed===")
                time.sleep(1)


lexobot = Lexobot(host=HOST, api_key=API_KEY, username=USERNAME)

if __name__ == "__main__":
    print(lexobot())
