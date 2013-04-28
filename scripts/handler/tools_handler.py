#coding=utf8
import sys
sys.path.append('../')
#from common.city_code_list import city_code_list
from common.yahoo_city_code_list import yahoo_city_code_list
from common.weather import get_weather


#weather_api = 'http://www.weather.com.cn/data/sk/%d.html'
#weather_api2 = 'http://www.weather.com.cn/data/cityinfo/%d.html'
#city_code_list = json.loads(city_code_list)

def weatherhandler(obj, action):
#    city_cname = action
#    city_code = city_code_list.get(city_cname)
#    if not city_code:
#        return '请用汉字输入城市名称'
#    url = weather_api2 % int(city_code)
#    info = json.loads(urllib2.urlopen(url).read())['weatherinfo']
#    #weather_info = json.loads(info.read())
#    res = u'''
#    %s,
#    %s - %s,
#    %s'''%(info['weather'], info['temp1'], info['temp2'], info['ptime'])
#    return res
    city_name = action
    city_code = yahoo_city_code_list.get(city_name)
    if not city_code:
        return "I can't understand your command. -_-"
    info = get_weather(city_code)
    current_info = info['forecasts'][0]
    tomorrow_info = info['forecasts'][1]
    tom = 'Tomorrow:\n'
    tom += 'Temp: ' + tomorrow_info['low'] + ' - '+ tomorrow_info['high'] + '\n'
    tom += tomorrow_info['condition']

    cur = 'Today:\n'
    cur += 'Temp: ' + current_info['low'] + ' - ' + current_info['high'] + '\n'
    cur += current_info['condition']
    res = '''\n%s\n\n%s'''%(cur.strip(), tom.strip())
    return res


