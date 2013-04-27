#coding=utf8
from hubot_script import *

class TestScript(HubotScript):
    
    @hear('def')
    def test_handler(self, message):
        return 'hear'
        
    #@respond('abc')
    #def test_handlera(self, message):
    #    return 'respond'
        
if __name__ == '__main__':
    test = TestScript()
