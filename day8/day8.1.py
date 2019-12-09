#!/usr/bin/env python

W, H = 25, 6
a = list(map(int, list(open('in.txt').read().strip())))
al, pos = len(a), 0
min_layer, min_num_zeroes = None, 0

while pos + 1 < al:
    layer = a[pos:pos + (W * H)]
    num_zeroes = sum(1 for i in layer if i == 0)
    if min_layer is None or num_zeroes < min_num_zeroes:
        min_layer, min_num_zeroes = layer, num_zeroes
    pos += (W * H)

num_ones = sum(1 for i in min_layer if i == 1)
num_twos = sum(1 for i in min_layer if i == 2)
print(num_ones * num_twos)
