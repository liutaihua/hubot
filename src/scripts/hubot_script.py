#coding=utf8
import json
import re
import sys
import time

from handler.sys_handler import syscmdhandler 
from handler.chat_handler import chathandler 

handlers = [
    (r'/hubot/sys/(.*)', syscmdhandler),
    (r'/hubot/chat/(.*)', chathandler),
]

class HubotScript:
    def __init__(self):
        self.start_listening()

    # 创建一个listen, 监听标准输入, 有输入时执行后面逻辑
    def start_listening(self):
        while True:
            line = sys.stdin.readline()
            self.receive(line)

    def receive(self, json_str):
        # 这里一定需要捕获错误, 否则出错会直接跳出 start_listening中的循环, 监听就结束了
        try:
            json_dict = json.loads(json_str)
            json_dict['message'] = '/' + '/'.join(json_dict['message'].split(' ')) # 搞成类似url的形式, 方便handlers里的regex匹配
            self.dispatch(json_dict)
        except Exception, e:
            print e
            
    def send(self, message):
        if message:
            #print json.dumps(message)
            sys.stdout.write(json.dumps(message) + '\n')
            sys.stdout.flush()

    # Message Dispatch
    def dispatch(self, json_dict):
        #msg_type = json_dict['type']
        #if msg_type == 'hear':
        #    self.dispatch_generic(json_dict, _hear_handlers)
        #elif msg_type == 'respond':
        #    self.dispatch_generic(json_dict, _resp_handlers)
        self.dispatch_generic(json_dict, handlers)

    def dispatch_generic(self, message, regexes):
        for regex, handler in regexes:
            p = re.match(regex, message['message'])
            if p:
                action = ' '.join(p.groups()[0].split('/'))
                response = message
                #response_text = handler(self, message)
                response_text = handler(self, action)
                if response_text:
                    if len(response_text) > 3000: # nodejs的JSON.parse不能处理太长的str
                        response_text = response_text[:3000]
                    response['message'] = response_text
                    self.send(response)

    def no_handler(self, message):
        pass

# Decorators

def hear(regex):  
    def decorator(handler):
        handlers.append((regex, handler))
    return decorator  

#def respond(regex):  
#    def decorator(handler):
#        _resp_handlers.append((regex, handler))
#    return decorator
