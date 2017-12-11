puzInput = []

for x in open("10_input.txt").readline():
  puzInput.append(ord(x))

puzInput.extend([17, 31, 73, 47, 23])

l = []
for x in range(0, 256):
  l.append(x)

pos = 0
skipSize = 0

for x in range(0, 64):
  for length in puzInput:
    length = int(length)
    sublis = []
    upperBound = (pos+length) % (len(l))
    if upperBound < pos:
      sublis = l[pos:]
      sublis += (l[:upperBound])
      sublis.reverse()
      for x in range(pos, upperBound+len(l)):
        l[x%len(l)] = sublis[x-pos]
    else:
      sublis = l[pos:pos+length]
      sublis.reverse()
      for x in range(pos, pos + length):
        l[x] = sublis[x-pos]
    
    pos = (pos+length+skipSize) % len(l)
    skipSize += 1

denseHash = []
denseHex = ""
for x in range(0,16):
  subList = l[x*16:(x+1)*16]
  n = subList[0]
  for m in range(1, 16):
    n = n ^ subList[m]
  denseHash.append(n)
  hexNum = hex(n)[2:]
  if len(hexNum) == 1:
    hexNum = "0" + hexNum
  denseHex += (hexNum)

print denseHex

# I encountered mistakes around converting the number to hex, with removing the leading '0x'.
  # I used trim("0x"), which removes *all* zeroes.  Bad.
  # I also tripped up by appending the zero instead of prepending the zero.  The examples helped me realize this.
# I had to do some testing to gain confidence that my last for loop would work, but I got it right on the first try.