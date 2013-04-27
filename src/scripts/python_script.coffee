# Description:
#   A generic Hubot script that allows you to write Hubot scripts in Python.
#
# Commands:
#   hubot  sys  <Commands>    #执行一个系统命令

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
            send_to_python(msg.message.text, msg.message.room, 'hear')
            @robot.msg = msg

    send_to_python = (message, room, method) ->
        dict = 
            type : method,
            message : message,
            room : room
        python_script.stdin.write(JSON.stringify(dict) + '\n')
        console.log JSON.stringify(dict)

    receive_from_python = (json) ->
        data = JSON.parse(json)
        #@robot.messageRoom data.room, data.message # 恶心的问题, data.room在send_to_python调用传的参数msg.message.room是undefined, 导致这里不能这样用
        @robot.msg.send data.message   # 于是在入口的地方直接把msg对象赋给@robot里的, 在这里就能夸函数调用msg.send了.
