from pydiscourse import DiscourseClient
from bs4 import BeautifulSoup
import re


def htmlStripper(text: str):
    soup = BeautifulSoup(text, 'html.parser')
    soup = soup.get_text()
    new_text = re.sub('@', '', soup)
    return new_text


def getNotifications(client: DiscourseClient):
    return client._get('notifications.json')['notifications']


def getTopicReplyNumber(client: DiscourseClient):
    return client._get('notifications.json')['notifications'][0]['topic_id']


def getPostReplyNumber(client: DiscourseClient):
    return client._get('notifications.json')['notifications'][0]['post_number']


def getPostReplyContent(client: DiscourseClient):
    notification: dict = client._get('notifications.json')[
        'notifications'][0]
    post_id: int = notification['data']['original_post_id']
    topic_id: int = notification['topic_id']

    return client.post(topic_id=topic_id, post_id=post_id)['post_stream']['posts'][len(client.post(topic_id=topic_id, post_id=post_id)['post_stream']['posts']) - 1]['cooked']
