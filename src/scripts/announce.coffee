# Description:
#   Send messages to all chat rooms.
#
# Dependencies:
#   None
#
# Configuration:
#   HUBOT_ANNOUNCE_ROOMS - comma-separated list of rooms
#
# Commands:
#   hubot announce "<message>" - Sends a message to all hubot rooms.
#   hubot announce downtime for "<service>" starting <timeframe> - Syntactic sugar for announcing downtime commencement
#   hubot announce downtime complete for "<service>" - Syntactic sugar for announcing downtime completion
#
# Author:
#   Morgan Delagrange
#
# URLS:
#   /broadcast/create - Send a message to designated, comma-separated rooms.

is_admin_user = (userid) ->
  if userid == 'defage@gmail.com'
    return true
  else
    return false

module.exports = (robot) ->

  if process.env.HUBOT_ANNOUNCE_ROOMS
    allRooms = process.env.HUBOT_ANNOUNCE_ROOMS.split(',')
  else
    allRooms = []

  robot.respond /announce (.*)/i, (msg) ->
    if not is_admin_user(msg.message.user.id)
      msg.send "Forbidden, you ar not admin."
      return
    announcement = msg.match[1]
    for own key, user of robot.brain.data.users
      user_info = { user: user } # 总之, 为了后面robot和adapter的send方法调用, 多包一层, 否则send取user会取成undefined
      robot.send user_info, announcement
    
    #for room in allRooms
    #  robot.messageRoom room, announcement
    #  #robot.messageRoom 'defage', announcement

  robot.router.post "/broadcast/create", (req, res) ->
    if req.connection.remoteAddress != '127.0.0.1'
      res.end "Forbidden, Must from localhost"
      return
    for own key, user of robot.brain.data.users
      user_info = { user: user } # 总之, 为了后面robot和adapter的send方法调用, 多包一层, 否则send取user会取成undefined
      robot.send user_info, req.body.message
    res.end "Message Sent"
    #if req.body.rooms
    #  rooms = req.body.rooms.split(',')
    #else
    #  rooms = allRooms

    #for room in rooms
    #  robot.messageRoom room, req.body.message
    #res.end "Message Sent"
