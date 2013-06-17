#coding=utf8

def chathandler(self, action, args_list):
    if action in ['hi', 'hello', '你好', 'hello world']:
        res = '''
        How are you doing, lady. I'm Blabla.LTH robot!
        Is anybody need help?

        Input 'Help' to get help info.
        '''
        return res
