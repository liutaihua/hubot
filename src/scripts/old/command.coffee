# Description:
#   Email from hubot to any address
#
# Dependencies:
#   None
#
# Configuration:
#   None
#
# Commands:
#   hubot defage cmd <commands> 执行系统命令, 请勿滥用..
#
# Author:
#   liutaihua
#
# Additional Requirements
#   unix mail client installed on the system

util = require 'util'
child_process = require 'child_process'
exec = child_process.exec

module.exports = (robot) ->
  # 执行系统命令
  robot.hear /cmd (.*)/i, (msg) ->
    if msg.match[1] == 'top'
      exec 'top -bn 1', (error, stdout, stderr) ->
        msg.send stdout
    exec msg.match[1], (error, stdout, stderr) ->
      msg.send stdout

  robot.hear /sys (.*)/i, (msg) ->
    #term   = "\"#{msg.match[1]}\""
    term = msg.match[1]
    cmd = """python /root/app/hubot/process.py --action '#{term}'"""
    exec cmd, (error, stdout, stderr) ->
      msg.send stdout

