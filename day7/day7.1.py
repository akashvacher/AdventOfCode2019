#!/usr/bin/env python
import logging
from itertools import permutations

logging.basicConfig(level=logging.WARN)

op_to_param = {1: 3, 2: 3, 3: 1, 4: 1, 5: 2, 6: 2, 7: 3, 8: 3, 99: 0}


class Computer:
    def __init__(self):
        self.ip = 0

    def get_item(self, a):
        i = a[self.ip]
        self.ip += 1
        return i

    def op_exec(self, op, params, mode, a, IN, OUT, address=None):
        if op == 1:
            a[address] = sum(params)
            logging.info(
                f"1 - Adding {params} and storing solution ({a[address]}) at index {address}"
            )

        if op == 2:
            ans = 1
            for i in params:
                ans *= i
            a[address] = ans
            logging.info(
                f"2 - Multiplying {params} and storing solution ({a[address]}) at index {address}"
            )

        if op == 3:
            inp = next(IN)
            a[address] = inp
            logging.info(f"3 - Storing input {inp} at index {address}")

        if op == 4:
            OUT.append(params[0])
            logging.info(f"4 - Producing output {OUT[-1]}")

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
            logging.info(f"7 - Checking if {params[0]} is less that {params[1]}")
            a[address] = 1 if (params[0] < params[1]) else 0

        if op == 8:
            logging.info(f"8 - Checking if {params[0]} is equal to {params[1]}")
            a[address] = 1 if (params[0] == params[1]) else 0

    def compute(self, a, inp):
        """
        Accept an intcode program and an input stream (as a lists of integers)
        and return the final output stream after running the program
        """
        IN = iter(inp)
        OUT = []
        logging.info(f"Array state before we begin:\n{a}")
        while True:
            instruction = self.get_item(a)
            if instruction < 0:
                raise ValueError(
                    f"Invalid instruction encountered: {instruction}\nInstruction pointer: {self.ip}\nProgram state: {a}"
                )

            op = instruction % 100
            mode = instruction // 100

            # Invalid opcode check
            if op not in op_to_param.keys():
                raise ValueError(
                    f"Invalid instruction encountered: {instruction}\nInstruction pointer: {self.ip}\nProgram state: {a}"
                )

            # Halt opcode
            if op == 99:
                logging.info("Halting now")
                break

            param_count = op_to_param[op]
            params = [self.get_item(a) for i in range(param_count)]
            address = None
            if op in (1, 2, 3, 7, 8):
                # Isolate last param as it's the address
                address = params.pop()
                param_count -= 1

            # Convert params to usable values depending on whether they are
            # in "position" mode or "immediate" mode.
            for i in range(param_count):
                if mode % 10 == 0:
                    params[i] = a[params[i]]
                mode //= 10

            self.op_exec(op, params, mode, a, IN, OUT, address)
        return OUT


def load_input():
    return list(map(int, open("in.txt").read().split(",")))


def get_thrust(phases, a):
    signal = 0
    for phase in phases:
        signal = Computer().compute(a[:], inp=[phase, signal])[0]
    return signal


def get_max_thrust(a):
    max_thrust = 0
    for phases in permutations(range(5)):
        logging.info(f"Trying: {phases}")
        max_thrust = max(max_thrust, get_thrust(phases, a))
    return max_thrust


a = load_input()
print(get_max_thrust(a))

