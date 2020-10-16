import os
from slack import WebClient
from slack.errors import SlackApiError


class SlackNotifier:
    def __init__(self, token, alert_channel='#alerts'):
        self.token = token
        self.alert_channel = alert_channel

    def message(self, msg):
        client = WebClient(token=self.token)
        try:
            response = client.chat_postMessage(
                channel=self.alert_channel,
                text=msg)
            print("response: ", response)
        except SlackApiError as e:
            # You will get a SlackApiError if "ok" is False
            assert e.response["ok"] is False
            assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
            print(f"Got an error: {e.response['error']}")




