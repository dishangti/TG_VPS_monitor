import os
from tg_bot import Bot
import json
from datetime import datetime

try:
	with open('settings.json', 'r') as f:
		settings = json.loads(f.read())
		servername = settings['servername']
		total_traffic = settings['total_traffic']
		traffic_method = settings['traffic_method']
except:
	pass

bot = Bot()

with open('./tg_stat_id.txt', 'r') as ids:
	for id in ids:
		id = int(id.strip())
		bot.delete_msg(id)

os.system('vnstati -i eth0 -m -o ./vnstat_m.png')
os.system('vnstati -i eth0 -s -o ./vnstat_s.png')

nowdate = str(datetime.now().year) + '年' + str(datetime.now().month) + '月' + str(datetime.now().day) + '日'
hello = servername + '\n节点总流量' + total_traffic + '(' + traffic_method + ')' + '\n今天是' + nowdate + '\n以下是当前流量统计信息：'

with open('./tg_stat_id.txt', 'w') as id:
	res = bot.send_text(hello)
	id.write(str(res['message_id']) + '\n')
	with open('./vnstat_s.png', 'rb') as f:
		res = bot.send_photo(photo = f)
		id.write(str(res['message_id']) + '\n')
	with open('./vnstat_m.png', 'rb') as f:
		res = bot.send_photo(photo = f)
		id.write(str(res['message_id']) + '\n')

os.system('rm -f ./vnstat_m.png')
os.system('rm -f ./vnstat_s.png')
