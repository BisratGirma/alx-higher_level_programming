#!/usr/bin/python3
def main(argv):
  argc = len(argv)
  operator = {
    '+': calculator_1.add,
    '-': calculator_1.sub,
    '/': calculator_1.div,
    '*': calculator_1.mul,
  }
  if argc != 4:
    print("Usage: {:s} <a> <operator> <b>".format(argv[0]))
    exit(1)
  a = int(argv[1])
  b = int(argv[3])
  operator = argv[2]
  if in_op not in '+-/*':
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
  res = operator[in_op](a, b)
  print("{:d} {:s} {:d} = {:d}".format(a, in_op, b, res))
  
  
  if __name__ == '__main__':
    from sys import argv, exit
    import calculator_1
    main(argv)
