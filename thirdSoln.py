# We have v=u+at where v is velocity, u is initial velocity, and t is time. And value for each is as follows: v=25m/s. u=0m/s, t=10 seconds. Find the acceleration a.

def acceleration(v=0, u=0, t=0):
    return (v - u) / t
print("The acceleration for v = {} , u = {} ,t={} is a = {}m/s".format('25m/s','0m/s','10second',acceleration(25,0,10)))