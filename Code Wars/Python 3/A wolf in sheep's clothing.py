def warn_the_sheep(queue):
    queue.reverse()
    
    for sheep in range(len(queue)):
        
        if queue[sheep] == "wolf" and sheep == 0:
            return "Pls go away and stop eating my sheep"
            
        elif queue[sheep] == "wolf":
            return "Oi! Sheep number %d! You are about to be eaten by a wolf!" % (sheep)
            
        else:
            pass