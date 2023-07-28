balls = ["red", "green", "green", "white", "blue", "red", "blue", "green", "white", "red", "red", "blue", "green", "blue", "violet", "green", "white", "red", "red", "blue", "red"]

#x = balls.count("red")
#y = balls.count("green")
#z = balls.count("white")
#a = balls.count("blue")
#b = balls.count("violet")

#print("red",x)
#print("green",y)
#print("white",z)
#print("blue",a)
#print("violet",b)

ball_list =[]
for ball in balls:
  if ball in ball_list:
    continue
  else:
    ball_list.append(ball)
    print(f"{ball} balls: {balls.count(ball)}")
