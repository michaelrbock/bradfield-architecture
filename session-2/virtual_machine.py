LOAD = 0x01
STORE = 0x02
ADD = 0x03
SUB = 0x04
HALT = 0xff


def run(memory):
  registers = [
    0x0000, # counter
    0x0000, # register_1
    0x0000  # register_2
  ]

  while True:
    pc_value = registers[0]
    op_code = memory[pc_value]

    if op_code == HALT:
      return

    op_arg1, op_arg2 = memory[pc_value + 1], memory[pc_value + 2]

    # Note: could use bit masks/shifting here instead.
    if op_code == LOAD:
      registers[op_arg1] = memory[op_arg2] + (256 * memory[op_arg2 + 1])
    elif op_code == STORE:
      memory[op_arg2] = registers[op_arg1] % 256
      memory[op_arg2 + 1] = registers[op_arg1] // 256
    elif op_code == ADD:
      registers[op_arg1] = registers[op_arg1] + registers[op_arg2]
    elif op_code == SUB:
      registers[op_arg1] = registers[op_arg1] - registers[op_arg2]
    else:
      raise ValueError('Invalid opcode')

    registers[0] += 3


if __name__ == '__main__':
  # 255 + 3
  program = [
    0x01, 0x01, 0x10, # LOAD r1 input1
    0x01, 0x02, 0x12, # LOAD r2 input2
    0x03, 0x01, 0x02, # ADD r1 + r2
    0x02, 0x01, 0x0e, # STORE r1 ouput 2
    0xff, # HALT
    0x00, # unused
    0x00, 0x00, # ouput
    0xff, 0x00, # 255
    0x03, 0x00 # 3
  ]

  run(program)
  assert(program[0x0e] == 2)
  assert(program[0x0f] == 1)

  # 5281 + 12
  program = [
    0x01, 0x01, 0x10, # LOAD r1 input1
    0x01, 0x02, 0x12, # LOAD r2 input2
    0x03, 0x01, 0x02, # ADD r1 + r2
    0x02, 0x01, 0x0e, # STORE r1 ouput 2
    0xff, # HALT
    0x00, # unused
    0x00, 0x00, # output
    0xa1, 0x14, # 5281
    0x0c, 0x00 # 12
  ]

  run(program)
  assert(program[0x0e] == 173)
  assert(program[0x0f] == 20)

  print('OK')
