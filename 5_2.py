l = []
for line in open('5-input.txt').readlines():
  l.append(int(line))
# l = [0,3,0,1,-3]

escape = False
idx = 0
numSteps = 0
while not escape:
  try:
    jmp = l[idx]
    if jmp >= 3:
      l[idx] -= 1
    else:
      l[idx] += 1
    idx += jmp
    numSteps += 1
  except IndexError:
    escape = True

print numSteps
