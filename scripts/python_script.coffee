# Description:
#   A generic Hubot script that allows you to write Hubot scripts in Python.
#   封装一个Python 类, 接收stdin, 输出stdout. 
#   在nodejs里启动这个py类的listen监听stdin, robot收到消息时write到stdin, 
#   py从stdin中读到消息, 交给指定的handler
#   handler处理完成后, 输出stdout, 同时触发nodejs的event, 读取stdout通过robot发送回馈信息.
#
# Commands:
#   hubot  sys  <Commands>    #执行一个系统命令
#
# Author:
#   liutaihua <defage@gmail.com>
#

ADMIN_LIST = new Array('defage@gmail.com')


class PythonScript
    pyScriptPath = __dirname + '/test.py'
    python_script = require('child_process').spawn('python', [pyScriptPath])
    python_script.stdout.on 'data', (data) =>
        receive_from_python(data.toString())

    module.exports = (robot) ->
        @robot = robot
        #robot.respond /(.*)/i, (msg) ->
        #    newRegex = new RegExp("^[@]?#{robot.name}[:,]? ?(.*)", 'i')
        #    match = newRegex.exec msg.message.text
        #    send_to_python(match[1], msg.message.room, 'respond')
        #    @robot.msg = msg

        robot.hear /(.*)/i, (msg) ->
            reSys = new RegExp('sys .*')
            if msg.message.user.id not in ADMIN_LIST and reSys.test(msg.match[1]) # 执行sys 系统命令的只能管理员
               msg.send "forbidden"
               return
            send_to_python(msg.message.text, msg.message.room, 'hear')
            @robot.msg = msg

        robot.router.get "/hubot/get/(?:.*)", (req, res) ->
            console.log req.route.path
            res.send 'success'

    send_to_python = (message, room, method) ->
        dict = 
            type : method,
            message : message.toLowerCase(),
            room : room
        python_script.stdin.write(JSON.stringify(dict) + '\n')
        console.log JSON.stringify(dict)

    receive_from_python = (json) ->
        data = JSON.parse(json)
        #@robot.messageRoom data.room, data.message # 恶心的问题, data.room在send_to_python调用传的参数msg.message.room是undefined, 导致这里不能这样用
        return @robot.msg.send data.message   # 于是在入口的地方直接把msg对象赋给@robot里的, 在这里就能夸函数调用msg.send了.
