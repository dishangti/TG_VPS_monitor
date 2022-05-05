import os
from tg_bot import Bot
import json
from datetime import datetime

os.chdir(os.path.dirname(__file__))

with open('settings.json', 'r') as f:
		settings = json.loads(f.read())
		servername = settings['servername']
		total_traff = settings['total_traff_stat']
		traff_methd = settings['traff_methd_stat']
		ifce = settings['ifce_stat']

bot = Bot()

try:		# 以防文件不存在炸了
	with open('./tg_stat_id.txt', 'r') as ids:
		for id in ids:
			id = int(id.strip())
			bot.delete_msg(id)
except:
	pass

os.system(f'vnstati -i {ifce} -m -o ./vnstat_m.png')
os.system(f'vnstati -i {ifce} -s -o ./vnstat_s.png')

nowdate = str(datetime.now().year) + '年' + str(datetime.now().month) + '月' + str(datetime.now().day) + '日'
hello = servername + '\n节点总流量' + total_traff + '(' + traff_methd + ')' + '\n今天是' + nowdate + '\n以下是当前流量统计信息：'

with open('./tg_stat_id.txt', 'w') as id:
	res = bot.send_text(hello)
	id.write(str(res['message_id']) + '\n')
	res = bot.send_image('./vnstat_s.png')
	id.write(str(res['message_id']) + '\n')
	res = bot.send_image('./vnstat_m.png')
	id.write(str(res['message_id']) + '\n')

os.system('rm -f ./vnstat_m.png')
os.system('rm -f ./vnstat_s.png')
