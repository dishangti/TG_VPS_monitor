# TG_VPS_monitor
VPS性能监控轻量脚本，自动将报告和预警信息自动通过Telegram Bot上传

### 依赖项
系统工具：vnstat, vnstati

Debian和Ubuntu可通过以下命令安装：

`apt-get install vnstat vnstati`

Python库：python-telegram-bot, psutil

通过以下命令安装：

`pip install python-telegram-bot psutil`

### 配置文件
配置文件为`settings.json`根据注释填入对应信息即可

由于JSON不支持注释，我把注释放在这里
```json
{
    "bot_token": "",        //Telegram机器人Token
    "chat_id": "",          //Chat ID (你可以从@getmyid_bot获取)
    "servername": "",       //你想如何称呼你的服务器
    "traffic_method": "",   //节点流量计算方式（单向计算、双向计算等）
    "total_traffic": "",    //每月总流量（800G）

    "cpu_warn": 75,         //CPU占用率告警阈值，设置为0不进行检测
    "mem_warn": 80,         //内存占用率告警阈值，设置为0不进行检测
    "conn_warn": 1000,      //TCP连接数告警阈值，设置为0不进行检测
    "disk_warn": 1024       //磁盘剩余空间告警阈值(MB)，设置为0不进行检测
}
```

### 定时执行
可以通过crontab配置定时执行，其中`tg_stat.py`文件为统计报告，`tg_warn.py`文件为预警报告

配置`crontab -e`加入如下计划任务
```shell
0 8 * * * /usr/bin/python3 /root/tg_stat.py
*/15 * * * * /usr/bin/python3 /root/tg_warn.py
```
即可每天早上八点发送统计报告，每隔15分钟检测系统性能状态。
