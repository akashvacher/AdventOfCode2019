#!/usr/bin/env python
import logging
logging.basicConfig(level=logging.WARN)

op_to_param = {
    1: 3,
    2: 3,
    3: 1,
    4: 1,
    99: 0
}


class Computer():
    def __init__(self):
        self.ip = 0

    def get_item(self):
        i = a[self.ip]
        self.ip += 1
        return i

    def op_exec(self, op, params, address, mode, a, IN, OUT):
        if op == 1:
            a[address] = sum(params)
            logging.info(f"1 - Adding {params} and storing solution ({a[address]}) at index {address}")

        if op == 2:
            ans = 1
            for i in params:
                ans *= i
            a[address] = ans
            logging.info(f"2 - Multiplying {params} and storing solution ({a[address]}) at index {address}")

        if op == 3:
            inp = next(IN)
            a[address] = inp
            logging.info(f"3 - Storing input {inp} at index {address}")

        if op == 4:
            if mode == 0:
                OUT.append(a[address])
            else:
                OUT.append(address)
            logging.info(f"4 - Producing output {OUT[-1]}")

    def compute(self, a, inp):
        '''
        Accept an intcode program and an input stream (as a lists of integers)
        and return the final output stream after running the program
        '''
        IN = iter(inp)
        OUT = []
        logging.info(f"Array state before we begin:\n{a}")
        while True:
            instruction = self.get_item()
            if instruction < 0:
                raise ValueError(f"Invalid instruction encountered: {instruction}\nInstruction pointer: {self.ip}\nProgram state: {a}")

            op = instruction % 100
            mode = instruction // 100

            # Invalid opcode check
            if op not in op_to_param.keys():
                raise ValueError(f"Invalid instruction encountered: {instruction}\nInstruction pointer: {self.ip}\nProgram state: {a}")

            # Halt opcode
            if op == 99:
                logging.info("Halting now")
                break

            param_count = op_to_param[op]
            params = [self.get_item() for i in range(param_count)]

            # Isolate last param as it's usually the address
            address = params.pop()
            param_count -= 1

            # Convert params to usable values depending on whether they are
            # in "position" mode or "immediate" mode.
            for i in range(param_count):
                if mode % 10 == 0:
                    params[i] = a[params[i]]
                mode //= 10

            self.op_exec(op, params, address, mode, a, IN, OUT)
        return OUT


def load_input():
    return list(map(int, open('in.txt').read().split(',')))


a = load_input()
print(Computer().compute(a, inp=[1]))
