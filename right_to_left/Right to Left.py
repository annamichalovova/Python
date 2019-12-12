def left_join(phrases):
    
   return ','.join(phrases).replace("right","left")

print(left_join(("left", "right", "left", "stop")))
