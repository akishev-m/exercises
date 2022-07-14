#!/usr/bin/env python

import copy
import os
from hexlet.fs import mkdir, mkfile, get_children, get_meta, is_file, get_name, is_directory, flatten


def find_files_by_name(tree, string):
    def walk(node, string, ancestry):
        name = get_name(node)
        children = get_children(node)
        if is_file(node) and string in name:
            return os.path.join(ancestry, name)
        output = map(
                lambda child: walk(child, string, os.path.join(ancestry, name)), children)
        return flatten(output)
    return walk(tree, string, '/')


def main():
    tree = mkdir('/', [
        mkdir('etc', [
            mkdir('apache'),
            mkdir('nginx', [
                mkfile('.nginx.conf', {'size': 800}),
            ]),        
            mkdir('.consul', [
                mkfile('.config.json'),
                mkfile('data'),
                mkfile('raft'),
            ]),
        ]),
        mkfile('hosts', {'size': 3500}),
        mkfile('resolve', {'size': 1000}),
    ])

    print((tree))
    print('------------------')
    print(find_files_by_name(tree, 'co'))

if __name__ == '__main__':
    main()
