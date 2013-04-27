# Description:
#   Utility commands surrounding Hubot uptime.
#
# Commands:
#   hubot ip <IP> - IP归属地信息查询


util = require 'util'
child_process = require 'child_process'
exec = child_process.exec

module.exports = (robot) ->
  robot.respond /HI$/i, (msg) ->
    msg.send "你好"

  robot.respond /ECHO (.*)$/i, (msg) ->
    msg.send msg.match[1]

  robot.respond /DIE$/i, (msg) ->
    msg.send "Goodbye, cruel world."
    process.exit 0

  robot.hear /ip (.*)/i, (msg) ->
    ip = msg.match[1]
    cmd = """python /root/app/hubot/process.py --action 'get_ipinfo #{ip}'"""
    exec cmd, (error, stdout, stderr) ->
      msg.send stdout
