import os
import time
from tg_bot import Bot
import psutil
import json
from datetime import datetime

try:
	with open('settings.json', 'r') as f:
		settings = json.loads(f.read())
		servername = settings['servername']
		total_traffic = settings['total_traffic']
		traffic_method = settings['traffic_method']

		cpu_warn = settings['cpu_warn']
		mem_warn = settings['mem_warn']
		disk_warn = settings['disk_warn']
		conn_warn = settings['conn_warn']
except:
	pass

bot = Bot()

nowdate = nowdate = str(datetime.now().year) + '年' + str(datetime.now().month) + '月' + str(datetime.now().day) + '日'\
	+ str(datetime.now().hour) + ":" + str(datetime.now().minute) + ":" + str(datetime.now().second)

headinfo = nowdate + '\n' + servername + '\n'

### 连接数监测
with os.popen('netstat -nt | wc -l') as f:
	res = int(f.readline())
if res >= conn_warn:
	with os.popen("netstat -n | awk '/^tcp/ {++S[$NF]} END {for(a in S) print a, S[a]}'") as f:
		status = f.read()
	bot.send_text(text = headinfo + 'TCP连接数异常，当前状态：\n' + status)

### CPU监测
time.sleep(2)		# 由于CPU占用波动性大，此处采用双延迟双检测
res = psutil.cpu_percent()
if res >= cpu_warn:
	time.sleep(30)
	res = psutil.cpu_percent()
	if res >= 75:
		with os.popen("ps axo user,pcpu,cmd --sort -pcpu | head -n 11") as f:
			status = f.read()
		bot.send_text(text = headinfo + 'CPU占用率' + str(res) + '异常，当前占用Top10：\n' + status)

### 内存监测
mem = psutil.virtual_memory()
res = float(mem.percent)
if res >= mem_warn:
	with os.popen("ps axo user,pmem,cmd --sort -pmem | head -n 11") as f:
		status = f.read()
	bot.send_text(text = headinfo + '内存占用率' + str(res) + '异常，当前占用Top10：\n' + status)

### 磁盘剩余监测（根目录）
disk  = os.statvfs('/')
res = disk.f_bsize * disk.f_bavail / 1024 / 1024
if res < disk_warn:
	with os.popen("df -h") as f:
		status = f.read()
	bot.send_text(text = headinfo + '磁盘剩余' + str(res) + '异常，当前状态：\n' + status)
