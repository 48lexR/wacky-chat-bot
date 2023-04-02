from pydiscourse import DiscourseClient
from bs4 import BeautifulSoup
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
                print(htmlStripper(getPostReplyContent(client)))

                # client.create_post(
                #     "This is a dummy message! In order to further communicate with me, I need more practice!", getPostReplyNumber(client), getTopicReplyNumber(client))

                print(getReplyType(client=client))
                time.sleep(1)

            # time.sleep(0.01)
    # client.create_post("Hello! I'm Lexobot. I'm still learning to wield the power of my own existence, so please bear with me!",
    #                    TESTING_CATEGORY, TESTING_THREAD)


lexobot = Lexobot(host=HOST, api_key=API_KEY, username=USERNAME)

if __name__ == "__main__":
    print(lexobot())
