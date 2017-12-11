puzInput = open("10_input.txt").readline().split(',')
# puzInput = open("10_example.txt").readline().split(',')
# puzInput = [2]

l = []
for x in range(0, 256):
  l.append(x)
# for x in range(0, 5):
#   l.append(x)

pos = 0
skipSize = 0

for length in puzInput:
  length = int(length)
  sublis = []
  upperBound = (pos+length) % (len(l))

  # print l 
  # print "becomes"
  if upperBound < pos:
    sublis = l[pos:]
    sublis += (l[:upperBound])
    sublis.reverse()
    for x in range(pos, upperBound+len(l)):
      # print "index " + str(x%len(l)) + " is gonna be " + str(sublis[x-pos])
      l[x%len(l)] = sublis[x-pos]
  else:
    sublis = l[pos:pos+length]
    sublis.reverse()
    for x in range(pos, pos + length):
      l[x] = sublis[x-pos]
  
  # print l

  pos = (pos+length+skipSize) % len(l)
  skipSize += 1

# print l
# print l[pos]
# print skipSize
print l[0] * l[1]