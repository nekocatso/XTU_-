
import requests
import json

def sender():
    url = 'https://app.xiaoyuan.ccb.com/channelManage/outbreak/addOutbreak'

    # ------------------------------------------------------------------------------------------------
    # 把抓包获得的cookie放到下面的引号里面来
    cookies = ""
    # ------------------------------------------------------------------------------------------------

    # 触发器设置使用的是cron表达式
    # 0 0 6 * * * *
    # 表示每天早上6点打卡，如果要改成8点打卡就改成
    # 0 0 8 * * * *
    # 如果想改其他的，自行使用在线生成器：https://cron.qqe2.com/

    headers = {
        'Host': 'app.xiaoyuan.ccb.com',
        'Connection': 'keep-alive',
        'Content-Length': '1185',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; YAL-AL10 Build/HUAWEIYAL-AL10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.185 Mobile Safari/537.36jianronghuixue/1.2.2',
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'https://app.xiaoyuan.ccb.com',
        'X-Requested-With': 'com.ccb.xiangdaxiaoyuan',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://app.xiaoyuan.ccb.com/LHECRESM/DZK/index2020110601.html',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-CN;q=0.8,en-US;q=0.7,en;q=0.6',
        'Cookie': cookies
        }
    null = ''
    # ------------------------------------------------------------------------------------------------
    # 把抓包获取的数据直接放到下面的等于号后面
    data = {""}
    # ------------------------------------------------------------------------------------------------
    data = json.dumps(data)
    res = requests.post(url=url, data=data, headers=headers)
    return res.text


def main_handler(event, context):
    return sender()


if __name__ == '__main__':
    sender()
