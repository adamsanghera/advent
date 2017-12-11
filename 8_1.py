registers = {}

def evalCond(cond, condReg, condNum):
  if cond == "==":
    return registers[condReg] == condNum
  elif cond == ">=":
    return registers[condReg] >= condNum
  elif cond == "<=":
    return registers[condReg] <= condNum
  elif cond == "<":
    return registers[condReg] < condNum
  elif cond == ">":
    return registers[condReg] > condNum
  elif cond == "!=":
    return registers[condReg] != condNum
  else:
    print "HUGE ERROR WATCH OUT"

maxValue = 0

for line in open('8_input.txt').readlines():
  command, cond = line.split("if")
  reg, comm, num = command.split()
  num = int(num)

  condReg, cond, condNum = cond.split()
  condNum = int(condNum)

  # print reg + ":"  + comm + ":" + str(num) + ":" + condReg + ":" + cond + ":" + str(condNum) + ":"

  if reg not in registers.keys():
    print "Adding " + reg + " to the dict"
    registers[reg] = 0
  if condReg not in registers.keys():
    print "Adding " + condReg + " to the dict"
    registers[condReg] = 0

  if evalCond(cond, condReg, condNum):
    if comm == "inc":
      registers[reg] += num
      if registers[reg] >= maxValue:
        maxValue = registers[reg]
    elif comm == "dec":
      registers[reg] -= num
      if registers[reg] >= maxValue:
        maxValue = registers[reg]

print max(registers.values())
print maxValue