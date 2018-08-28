from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory
"""
from .views import index

class SimpleTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

    def test_details(self):
        # Create an instance of a GET request.
        request = self.factory.get('/')
        request.user = AnonymousUser()

        # Test my_view() as if it were deployed at /customer/details
        response = index(request)
        self.assertEqual(response.status_code, 200)
        """
import requests
import datetime


class IrisMath:


    def __init__(self, token):
        self.token = "410791967:AAE9k6Md42v3dtMSzW3jroF_3umKaWfaxvo"
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def search_dialogue2(self):
        data = IrisMath.get_updates()
        users_names = {}
        user_data = {}
        text = []
        name = 0
        results = data['result']
        for row in results:
            name = row['message']['chat']['first_name']
            this_chat_id = row['message']['chat']['id']
            this_text = row['message']['text']
            if name == 'Nastya':
                print(this_text)

    def send_message_to_N(self, text):
        chat_id = 516555131
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            #last_update = get_result[len(get_result)]
            last_update = None

        return last_update

token = "410791967:AAE9k6Md42v3dtMSzW3jroF_3umKaWfaxvo"
iris_bot = IrisMath(token)
greetings = ('здравствуй', 'привет', 'ку', 'здорово', 'хай', 'добрый', 'здаров', 'здаровки')
now = datetime.datetime.now()


def main():

    new_offset = None
    today = now.day
    hour = now.hour


    time = datetime.time
    time = str(now)
    dazzle = 	u"\U0001F61D"
    drizzle = 	u"\U0001F60A"
    hearts=[u"\u2764", u"\U0001F49B", u"\U0001F49A",u"\U0001F499",u"\U0001F49C"]

    while True:

        iris_bot.get_updates(new_offset)

        last_update = iris_bot.get_last_update()

        if not last_update:
            print("TWO")
            continue
        else:
            print("THREE")
            last_update_id = last_update['update_id']
            last_chat_text = last_update['message']['text']
            last_chat_id = last_update['message']['chat']['id']
            last_chat_name = last_update['message']['chat']['first_name']

        #last_update_id = last_update['update_id']


        if last_chat_text.lower() in greetings and today == now.day and 0 <= hour < 6:
            iris_bot.send_message(last_chat_id, 'Доброй ночи, {}'.format(last_chat_name))
            #today += 1

        if last_chat_text.lower() in greetings and today == now.day and 6 <= hour < 12:
            iris_bot.send_message(last_chat_id, 'Доброе утро, {}'.format(last_chat_name))
            #today += 1

        elif last_chat_text.lower() in greetings and today == now.day and 12 <= hour < 17:
            iris_bot.send_message(last_chat_id, 'Добрый день, {}'.format(last_chat_name))
            #today += 1

        elif last_chat_text.lower() in greetings and today == now.day and 17 <= hour < 23:
            iris_bot.send_message(last_chat_id, 'Добрый вечер, {}'.format(last_chat_name))
            #today += 1

        elif last_chat_text.lower() == 'ладно':
            iris_bot.send_message(last_chat_id, u"\u2764"  u"\u2764" u"\u2764" u"\u2764" u"\u2764" u"\u2764"u"\u2764""\n"
                                                 u"\U0001F49B" u"\U0001F49B"u"\U0001F49B"u"\U0001F49B"u"\U0001F49B" u"\U0001F49B"u"\U0001F49B""\n"
                                                 u"\U0001F49A" u"\U0001F49A"u"\U0001F49A"u"\U0001F49A"u"\U0001F49A" u"\U0001F49A" u"\U0001F49A" "\n"
                                                 u"\U0001F499"  u"\U0001F499"u"\U0001F499"u"\U0001F499"u"\U0001F499" u"\U0001F499" u"\U0001F499" "\n"
                                                 u"\U0001F49C" u"\U0001F49C" u"\U0001F49C" u"\U0001F49C" u"\U0001F49C"  u"\U0001F49C"  u"\U0001F49C" "\n" )

        new_offset = last_update_id + 1

  


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()

