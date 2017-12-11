# I *totally* cheated with this one

# Dict mapping node_name to parent_name, weight, [children]
nodes = {}

for line in open('7_input.txt').readlines():
  l = line.split("->")
  nodeInfo = l[0].split()
  children = []
  if len(l) > 1:
    children = l[1].split()
    for idx in range (0, len(children)):
      children[idx] = children[idx].strip(',')


  name = nodeInfo[0]
  weight = int((nodeInfo[1]).strip('(').strip(')'))

  if name not in nodes.keys():
    nodes[name] = ["", weight, children]
  else:
    nodes[name][1] = weight
    nodes[name][2] = children

  for c in children:
    if c not in nodes.keys():
      nodes[c] = [name, 0, []]
    else:
      nodes[c][0] = name

treeRoot = "mdbtyw"

def calcSubTowerWeight(root):
  if len(nodes[root][2]) == 0:
    return nodes[root][1]
  else:
    sum = nodes[root][1]
    for c in nodes[root][2]:
      sum += calcSubTowerWeight(c)
    return sum 

for c in nodes[treeRoot][2]:
  print c + " : " + str(calcSubTowerWeight(c))

print str(nodes[treeRoot][1])