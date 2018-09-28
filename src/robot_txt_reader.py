import urllib.robotparser
from settings import robots_url
rp = urllib.robotparser.RobotFileParser()
rp.set_url(robots_url)
rp.read()
canitfetch = rp.can_fetch('mybot', robots_url)
print("can it fetch? - %s" % canitfetch)