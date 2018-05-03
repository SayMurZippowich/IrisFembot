import requests
import datetime

class BotHandler:



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
        data = BotHandler.get_updates()
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
            last_update = get_result[len(get_result)]

        return last_update

token = "410791967:AAE9k6Md42v3dtMSzW3jroF_3umKaWfaxvo"
greet_bot = BotHandler(token)
greetings = ('здравствуй', 'привет', 'ку', 'здорово','хай','добрый')
now = datetime.datetime.now()
time = datetime.time
time = str(now)
dazzle = 	u"\U0001F61D"
drizzle = 	u"\U0001F60A"
hearts=[u"\u2764", u"\U0001F49B", u"\U0001F49A",u"\U0001F499",u"\U0001F49C"]
#greet_bot.send_message_to_N("Привет, теперь я могу отвечать на последний "
 #                           "приветственный запрос (при запуске компилятора),"
   #                         " определяя время суток или фразу 'Ладно'"+dazzle)

#greet_bot.send_message_to_N("Сейчас " + time[10:16])
#greet_bot.send_message_to_N("Утро будет добрым"+drizzle)

last_update = greet_bot.get_last_update()

last_update_id = last_update['update_id']
last_chat_text = last_update['message']['text']
last_chat_id = last_update['message']['chat']['id']
last_chat_name = last_update['message']['chat']['first_name']

new_offset = None
today = now.day
hour = now.hour

if last_chat_text.lower() in greetings and today == now.day and 0 <= hour < 6:
    greet_bot.send_message(last_chat_id, 'Доброй ночи, {}'.format(last_chat_name))
    today += 1

if last_chat_text.lower() in greetings and today == now.day and 6 <= hour < 12:
    greet_bot.send_message(last_chat_id, 'Доброе утро, {}'.format(last_chat_name))
    today += 1

elif last_chat_text.lower() in greetings and today == now.day and 12 <= hour < 17:
    greet_bot.send_message(last_chat_id, 'Добрый день, {}'.format(last_chat_name))
    today += 1

elif last_chat_text.lower() in greetings and today == now.day and 17 <= hour < 23:
    greet_bot.send_message(last_chat_id, 'Добрый вечер, {}'.format(last_chat_name))
    today += 1

elif last_chat_text.lower() == 'ладно':
    greet_bot.send_message(last_chat_id, u"\u2764"  u"\u2764" u"\u2764" u"\u2764" u"\u2764" u"\u2764"u"\u2764""\n"
                                         u"\U0001F49B" u"\U0001F49B"u"\U0001F49B"u"\U0001F49B"u"\U0001F49B" u"\U0001F49B"u"\U0001F49B""\n"
                                         u"\U0001F49A" u"\U0001F49A"u"\U0001F49A"u"\U0001F49A"u"\U0001F49A" u"\U0001F49A" u"\U0001F49A" "\n"
                                         u"\U0001F499"  u"\U0001F499"u"\U0001F499"u"\U0001F499"u"\U0001F499" u"\U0001F499" u"\U0001F499" "\n"
                                         u"\U0001F49C" u"\U0001F49C" u"\U0001F49C" u"\U0001F49C" u"\U0001F49C"  u"\U0001F49C"  u"\U0001F49C" "\n" )



print(last_chat_text)
greet_bot.send_message_to_N(last_chat_text)
#print(greet_bot.get_last_update())
