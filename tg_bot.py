import json
import telegram

class Bot:
    def __init__(self):
        with open(r'./settings.json', 'r') as f:
            settings = json.loads(f.read())
        self.chat_id = settings['chat_id']
        self.bot = telegram.Bot(token = settings['bot_token_head'] + ':' + settings['bot_token_tail'])

    def send_text(self, text):
        return self.bot.send_message(chat_id = self.chat_id, text = text)
    
    def send_image(self, path):
        with open(path, 'wb') as f:
            return self.bot.send_photo(chat_id = self.chat_id, photo = f)
    
    def delete_msg(self, msg_id):
        self.bot.delete_message(chat_id = self.chat_id, message_id = msg_id)