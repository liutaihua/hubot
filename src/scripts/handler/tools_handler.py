#coding=utf8
import sys
sys.path.append('../')
from common.city_code_list import city_code_list
import json
import urllib2


weather_api = 'http://www.weather.com.cn/data/sk/%d.html'
weather_api2 = 'http://www.weather.com.cn/data/cityinfo/%d.html'
city_code_list = json.loads(city_code_list)
#for k, v in city_code_list.items():print k, v, type(k)

def weatherhandler(obj, action):
    city_cname = action
    city_code = city_code_list.get(city_cname)
    if not city_code:
        return '请用汉字输入城市名称'
    url = weather_api2 % int(city_code)
    info = json.loads(urllib2.urlopen(url).read())['weatherinfo']
    #weather_info = json.loads(info.read())
    res = u'''
    %s,
    %s - %s,
    %s'''%(info['weather'], info['temp1'], info['temp2'], info['ptime'])
    return res

