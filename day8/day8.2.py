#!/usr/bin/env python

W, H = 25, 6
a = list(map(int, list(open('in.txt').read().strip())))
al, pos = len(a), 0

# Start with a transparent picture
pic = [2 for i in range(W * H)]

while pos < al:
    pic_pos = pos % (W * H)
    if pic[pic_pos] == 2:
        pic[pic_pos] = a[pos]
    pos += 1

for i in range(H):
    print(''.join('*' if i == 1 else ' ' for i in pic[:W]))
    pic = pic[W:]
