from pydiscourse import DiscourseClient
from extra_functions import getNotifications, htmlStripper, getPostReplyContent, getTopicReplyNumber, getPostReplyNumber
import time
HOST = 'HOST'
API_KEY = 'APIKEY'
USERNAME = 'Lexobot'


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
        notifs: dict = getNotifications(client)
        while True:
            if getNotifications(client)[0] != notifs[0]:
                print(htmlStripper(getPostReplyContent(client)))

                client.create_post(
                    "This is a dummy message! In order to further communicate with me, I need more practice!", getPostReplyNumber(client), getTopicReplyNumber(client))
                notifs = getNotifications(client)

            time.sleep(0.01)
    # client.create_post("Hello! I'm Lexobot. I'm still learning to wield the power of my own existence, so please bear with me!",
    #                    TESTING_CATEGORY, TESTING_THREAD)
