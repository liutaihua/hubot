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
#   hubot email <user@email.com> -s <subject> -m <message> - Sends email with the <subject> <message> to address <user@email.com>
#
# Author:
#   earlonrails
#
# Additional Requirements
#   unix mail client installed on the system

util = require 'util'
child_process = require 'child_process'
exec = child_process.exec

module.exports = (robot) ->
  # email by pmail scripts
  robot.respond /email (.*) -s (.*) -m (.*)/i, (msg) ->
    mailCommand = """python /root/app/hubot/scripts/pmail.py -t '#{msg.match[1]}' -s '#{msg.match[2]}' -c '#{msg.match[3]}'"""
    exec mailCommand, (error, stdout, stderr) ->
      msg.send stdout
