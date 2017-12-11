import copy

l = []
inputStr = "5 1 10 0 1 7 13 14 3 12 8 10 7 12 0 6" 
# inputStr = "0 2 7 0"
for x in inputStr.split():
  l.append(int(x))

memory = {}

ctr = 0
cycleSize = 0

while True:
  # Remember the state we're at.
  lStr = ""
  for z in l:
    lStr += str(z) + ","
  if lStr not in memory:
    memory[lStr] = ctr
  else:
    cycleSize = ctr - memory[lStr]
    break

  # Find the max bank, and the value there
  maxBank = l.index(max(l))
  harvest = l[maxBank]
  
  # Reset the value to 0
  l[maxBank] = 0

  # Start iterating through list
  idx = maxBank + 1
  while harvest != 0:
    if idx == len(l):
      idx = 0
    l[idx] += 1
    harvest -= 1
    idx += 1
  
  ctr += 1

print cycleSize
