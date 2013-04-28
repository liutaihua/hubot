
def chathandler(self, action):
    if action == 'hi' or ' hi' in action:
        res = '''
        How are you doing, lady?
        I'm Blabla.LTH robot 
        Is anybody need help?
        Help list:

        help                                      Pint this info.
        translate <some word>                     Translate your word given between English to Chinese.
        email -s <subject> -m <content>           Send an email to somebody you given.
        sys <command>                             Execute a your command given.
        math <expression>                         A counter ^_^
        pug bomb N                                Get N pugs.
        pug me                                    Receive a pug.
        show users                                Display all users that hubot knows about.
        time                                      Reply with current time
        show storage                              Display the contents that are persisted in the brain
        '''
        return res
