# TG_VPS_monitor
VPS性能监控脚本，自动将报告和预警信息自动通过Telegram Bot上传

### 依赖项
系统工具：vnstat, vnstati
Debian和Ubuntu可通过以下命令安装：
`apt-get install vnstat vnstati`

Python库：python-telegram-bot, psutil
通过以下命令安装：
`pip install python-telegram-bot psutil`

### 配置文件
配置文件为`settings.json`根据注释填入对应信息即可

### 定时执行
可以通过crontab配置定时执行，其中`tg_stat.py`文件为统计报告，`tg_warn.py`文件为预警报告
配置`crontab -e`加入如下计划任务
```shell
0 8 * * * /usr/bin/python3 /root/tg_stat.py
*/15 * * * * /usr/bin/python3 /root/tg_warn.py
```
即可每天早上八点发送统计报告，每隔15分钟检测系统性能状态。
