# line = open('9_input.txt').readline()
line = open('9_input.txt').readline()

# Conditions:
# (1) In garbage
#     (a) Ignoring current input
#     (b) Ignore next output
#     (c) Exit the garbage
#     (d) Count for removing 
# (2) Not in garbage
#     (a) Going into a new group
#     (b) Coming out of the last group
#     (c) Going into garbage
#     (d) Separating one group from the next

enclosingScore = 0
tally = 0
toRemove = 0
ignoring = False
inGarbage = False
for c in line:
  if inGarbage:
    if ignoring:
      ignoring = False
      continue
    elif c == '!':
      ignoring = True
      continue
    elif c == '>':
      inGarbage = False
      continue
    else:
      toRemove += 1
      continue
  else: 
    if c == '{':
      enclosingScore += 1
      continue
    elif c == '}':
      tally += enclosingScore
      enclosingScore -= 1
      continue
    elif c == '<':
      inGarbage = True
      continue
    elif c == ',':
      continue

print toRemove