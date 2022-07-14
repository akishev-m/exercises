#!/usr/bin/env python

import copy
from hexlet.fs import mkdir, mkfile, get_children, get_meta, is_file, get_name


def get_nodes_count(node):
    if is_file(node):
        return 1
    children = get_children(node)
    descendant_counts = list(map(get_nodes_count, children))
    return 1 + sum(descendant_counts)

def main():
    tree = mkdir('/', [
        mkdir('eTc', [
            mkdir('NgiNx', [], {'size': 4000}),
            mkdir(
                'CONSUL',
                [mkfile('config.JSON', {'uid': 0})],
            ),
        ]),
        mkfile('HOSTS'),
    ])
    print( (tree))
    print('------------------')
    print(get_nodes_count(tree))

if __name__ == '__main__':
    main()
