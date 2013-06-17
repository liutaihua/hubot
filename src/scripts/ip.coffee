# Description:
#   Return Hubot's external IP address (via jsonip.com)
#
# Dependencies:
#   None
#
# Configuration:
#  None
# 
# Commands:
#   hubot ip - Returns Hubot server's external IP address 
#
# Author:
#   ndrake
     
module.exports = (robot) ->
  robot.respond /ip( (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}))?/i, (msg) ->
    ip = String(msg.match[1]).replace(/^\s+|\s+$/g, '')
    if ip
      msg.http("http://ip.taobao.com/service/getIpInfo.php?ip=#{ip}")
      .get() (err, res, body) ->
        json = JSON.parse(body).data
        switch res.statusCode
          when 200
            if json.city != ''
              origin = json.city
              isp = json.isp
            else
              origin = json.country
              isp = "unknown"
            msg.send "#{origin}, ISP: #{isp}."
          else
            msg.send "There was an error getting external IP (status: #{res.statusCode})."
    else
      msg.http("http://jsonip.com")
        .get() (err, res, body) ->
          json = JSON.parse(body)
          switch res.statusCode                                
            when 200
              msg.send "External IP address: #{json.ip}"
            else
              msg.send "There was an error getting external IP (status: #{res.statusCode})."
                

