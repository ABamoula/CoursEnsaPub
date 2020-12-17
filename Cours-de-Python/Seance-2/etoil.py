graph= '*'
for i in range(1,6):
     lin1 = graph.center(17/i,' ')
     if i == 1: lin2 = graph.center(9,'#').center(17,' ')
print(lin1,'\n' ,lin2)
print(len(lin1))
print(len(lin2))