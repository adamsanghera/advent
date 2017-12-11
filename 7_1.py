# Dict mapping node_name to parent_name, weight
nodes = {}

for line in open('7_input.txt').readlines():
  l = line.split("->")
  nodeInfo = l[0].split()
  children = []
  if len(l) > 1:
    children = l[1].split()


  name = nodeInfo[0]
  weight = int((nodeInfo[1]).strip('(').strip(')'))

  if name not in nodes.keys():
    nodes[name] = ["", weight]
  else:
    nodes[name][1] = weight

  for c in children:
    c = c.strip(',')
    if c not in nodes.keys():
      nodes[c] = [name, 0]
    else:
      nodes[c][0] = name

for n in nodes.keys():
  if nodes[n][0] == "":
    print n