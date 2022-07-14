#!/usr/bin/env python

import copy
from hexlet.fs import mkdir, mkfile, get_children, get_meta, is_file, get_name


def get_hidden_files_count(node):
    if is_file(node) and get_name(node).startswith('.'):
        return 1
    children = get_children(node)
    descendant_counts = list(map(get_hidden_files_count, children))
    return sum(descendant_counts)

def main():
    tree = mkdir('/', [
        mkdir('etc', [
            mkdir('apache'),
            mkdir('nginx', [
                mkfile('.nginx.conf', {'size': 800}),
            ]),
            mkdir('.consul', [
                mkfile('.config.json', {'size': 1200}),
                mkfile('data', {'size': 8200}),
                mkfile('raft', {'size': 80}),
            ]),
        ]),
        mkfile('.hosts', {'size': 3500}),
        mkfile('resolve', {'size': 1000}),
    ])
    print( (tree))
    print('------------------')
    print(get_hidden_files_count(tree))

if __name__ == '__main__':
    main()
