def calcTime(dist, speed):
    print("dist=",dist)
    print("speed=",speed)
    t = dist / speed
    t = round(t, 1)
    return t

print(calcTime(500, 100))
print(calcTime(speed=500, dist=100))

