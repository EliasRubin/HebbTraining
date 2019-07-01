#!/usr/bin/env python3
import json
import argparse
import sys


weight = [];
bias = 0;


if len(sys.argv) == 1:
    print('Error need the file')
    sys.exit(1)

try:
    with open(sys.argv[1]) as jsf:
        data = json.load(jsf)
        i = 0;
        for p in data['training']:
            weight.append(p[0] + p[1])
            weight[i] = weight[i] * data['target'][i]
            bias = bias + data['target'][i]
            print('Weight ' + str(i) + ': ' + str(weight[i]))
            i = i + 1
        jsf.close()
except FileNotFoundError:
    print('404 FILE NOT FOUND')
    exit(1)

print('Bias: ' + str(bias))


