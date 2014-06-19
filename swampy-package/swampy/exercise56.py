
from TurtleWorld import *
world = TurtleWorld()
bob = Turtle()
bob.delay = 0
bob.x=-150
bob.y=90

def koch(t, x):
  if x < 3:
    fd(t, x)
    return
  else:
    koch(t, x/3)
    lt(t, 60)
    koch(t, x/3)
    rt(t, 120)
    koch(t, x/3)
    lt(t, 60)
    koch(t, x/3)

#koch(bob, 500)


def snowflake(t, n):
  for i in range(3):
    koch(t, n)
    rt(t, 120)
snowflake(bob, 300)

wait_for_user()
