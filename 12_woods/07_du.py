#!/usr/bin/env python

import copy
from hexlet.fs import mkdir, mkfile, get_children, get_meta, is_file, get_name, is_directory


def get_files_size(node):
    if is_file(node):
        return get_meta(node).get('size')
    children = get_children(node)
    descendant_counts = list(map(get_files_size, children))
    return sum(descendant_counts)


def du(node):
    children = get_children(node)
    result = map(
            lambda child: (get_name(child), get_files_size(child)),
            children
            )
    sorted_result = sorted(list(result), key=lambda x: x[1], reverse=True )
    return sorted_result

def main():
    tree = mkdir('/', [
        mkdir('etc', [
            mkdir('apache'),
            mkdir('nginx', [
                mkfile('.nginx.conf', {'size': 800}),
            ]),
            mkdir('.consul', [
                mkfile('.config.json', {'size': 1200}),
                mkfile('file.tmp', {'size': 8200}),
                mkfile('data', {'size': 80}),
            ]),
        ]),
        mkfile('hosts', {'size': 3500}),
        mkfile('resolve', {'size': 10000}),
    ])

    tree2 = mkdir('new folder', [
        mkfile('data', {'size': 100}),
        mkfile('hosts', {'size': 200}),
        ])

    print((tree))
    print('------------------')
    print(get_files_size(tree))
    print(du(tree))

if __name__ == '__main__':
    main()
