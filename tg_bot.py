import json
import os
import telegram

class Bot:
    def __init__(self):
        os.chdir(os.path.dirname(__file__))
        with open(r'./settings.json', 'r') as f:
            settings = json.loads(f.read())
        self.chat_id = settings['chat_id']
        self.bot = telegram.Bot(token = settings['bot_token'])

    def send_text(self, text):
        return self.bot.send_message(chat_id = self.chat_id, text = text)
    
    def send_image(self, path):
        with open(path, 'rb') as f:
            return self.bot.send_photo(chat_id = self.chat_id, photo = f)
    
    def delete_msg(self, msg_id):
        self.bot.delete_message(chat_id = self.chat_id, message_id = msg_id)
