#!/usr/bin/env python
import logging
from itertools import permutations, cycle
from collections import deque

logging.basicConfig(level=logging.WARN)
op_to_param = {1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3, 9: 1, 99: 0}


class Computer:
    def __init__(self, a, inp):
        self.ip = 0
        self.a = a
        self.inp = deque(inp)
        self.out = deque([])
        self.base = 0

    def get_input(self):
        return self.inp.popleft()

    def append_input(self, x):
        self.inp.append(x)

    def append_output(self, x):
        self.out.append(x)

    def get_item(self):
        i = self.a[self.ip]
        self.ip += 1
        return i

    def op_exec(self, op, params, address=None):
        if op == 1:
            self.a[address] = sum(params)
            logging.info(
                f"1 - Adding {params} and storing solution ({self.a[address]}) at index {address}"
            )

        if op == 2:
            ans = 1
            for i in params:
                ans *= i
            self.a[address] = ans
            logging.info(
                f"2 - Multiplying {params} and storing solution ({self.a[address]}) at index {address}"
            )

        if op == 3:
            inp = self.get_input()
            self.a[address] = inp
            logging.info(f"3 - Storing input {inp} at index {address}")

        if op == 4:
            self.append_output(params[0])
            logging.info(f"4 - Producing output {params[0]}")

        if op == 5:
            logging.info(f"5 - Checking if {params[0]} is not equal to zero")
            if params[0] != 0:
                self.ip = params[1]
                logging.info(f"5 - Setting instruction Pointer to {self.ip}")

        if op == 6:
            logging.info(f"6 - Checking if {params[0]} is equal to zero")
            if params[0] == 0:
                self.ip = params[1]
                logging.info(f"6 - Setting instruction Pointer to {self.ip}")

        if op == 7:
            logging.info(
                f"7 - Checking if {params[0]} is less that {params[1]}")
            self.a[address] = 1 if (params[0] < params[1]) else 0

        if op == 8:
            logging.info(
                f"8 - Checking if {params[0]} is equal to {params[1]}")
            self.a[address] = 1 if (params[0] == params[1]) else 0

        if op == 9:
            logging.info(
                f"9 - Adjusting relative base by adding {params[0]} to it")
            self.base += params[0]

    def compute(self):
        """
        yield the output item after running the program
        """
        logging.info(f"Array state before we begin:\n{self.a}")
        while True:
            instruction = self.get_item()
            if instruction < 0:
                raise ValueError(
                    f"Invalid instruction encountered: {instruction}\nInstruction pointer: {self.ip}\nProgram state: {self.a}"
                )

            op = instruction % 100
            mode = instruction // 100

            # Invalid opcode check
            if op not in op_to_param.keys():
                raise ValueError(
                    f"Invalid instruction encountered: {instruction}\nInstruction pointer: {self.ip}\nProgram state: {self.a}"
                )

            # Halt opcode
            if op == 99:
                logging.info("Halting now")
                return

            param_count = op_to_param[op]
            params = [self.get_item() for i in range(param_count)]
            address = None
            if op in (1, 2, 3, 7, 8):
                # Isolate last param as it's the address
                address = params.pop()
                param_count -= 1

            # Convert params to usable values depending on whether they are
            # in "position" mode or "immediate" mode.
            for i in range(param_count):
                if mode % 10 == 0:
                    params[i] = self.a[params[i]]
                if mode % 10 == 2:
                    params[i] = self.a[self.base + params[i]]
                mode //= 10
            if address is not None and mode == 2:
                address += self.base
            self.op_exec(op, params, address)
            if len(self.out) > 0:
                yield self.out.popleft()


def load_input():
    return list(map(int, open("in.txt").read().split(",")))


a = load_input()
c = Computer(a + [0] * 1000, inp=[1])
print(list(c.compute())[0])
