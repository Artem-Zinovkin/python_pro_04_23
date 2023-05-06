from datetime import datetime
from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class SocialChannel:
    channel_type: str
    followers: int


@dataclass
class Post:
    message: str
    timestamp: int


class Abstract_Channel(ABC):
    @abstractmethod
    def post_to_channel(channel: SocialChannel, message: str):
        ...


class Youtube_Channel(Abstract_Channel):
    @staticmethod
    def post_to_channel(channel: SocialChannel, message: str):
        print(f"{message}: post to {channel.channel_type} ")


class Facebook_Channel(Abstract_Channel):
    @staticmethod
    def post_to_channel(channel: SocialChannel, message: str):
        print(f"{message}: post to {channel.channel_type}")


class Twitter_Channel(Abstract_Channel):
    @staticmethod
    def post_to_channel(channel: SocialChannel, message: str):
        print(f"{message}: post to {channel.channel_type}")


def time():
    dt = datetime.now()
    return datetime.timestamp(dt)


def post_a_message(channel: SocialChannel, message: str) -> None:
    if channel.channel_type == "youtube":
        post_a_message = Youtube_Channel()

    elif channel.channel_type == "facebook":
        post_a_message = Facebook_Channel()

    elif channel.channel_type == "twitter":
        post_a_message = Twitter_Channel()

    post_a_message.post_to_channel(channel=channel, message=message)


def process_schedule(posts: list[Post], channels: list[SocialChannel]) -> None:
    for post in posts:
        message, timestamp = post.message, post.timestamp
        for channel in channels:
            if timestamp <= time():
                post_a_message(channel, message)
