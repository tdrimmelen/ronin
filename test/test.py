from ronincontroller import controller
import json

controldatajson = '{"pan":1023, "tilt": 1023, "roll":1023}'

controldata = json.loads(controldatajson)

# Create an object fo the ronin controller
c = controller.Controller('/dev/ttyAMAS0')

# send the speed data. Values from 0 - 2047 where 1023 is 0 speed.
c.send_speed(controldata['pan'],controldata['tilt'],controldata['roll'])