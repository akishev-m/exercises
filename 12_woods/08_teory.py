#!/usr/bin/env python

import copy
from hexlet.fs import mkdir, mkfile, get_children, get_meta, is_file, get_name, is_directory, flatten


def find_empty_dir_paths(tree):
    def walk(node, depth):
        name = get_name(node)
        children = get_children(node)
        if len(children) == 0:
            return name
        if depth == 2:
            return []
        dir_paths = filter(is_directory, children)
        output = map(
                lambda child: walk(child, depth + 1), dir_paths,
                )
        return flatten(output)
    return walk(tree, 0)


def main():
    tree = mkdir('/', [
        mkdir('etc', [
            mkdir('apache'),
            mkdir('nginx', [
                mkfile('.nginx.conf'),
            ]),        
            mkdir('.consul', [
                mkfile('.config.json'),
                mkfile('file.tmp'),
                mkdir('data'),
            ]),
        ]),
        mkdir('logs'),
        mkfile('hosts'),
    ])

    print((tree))
    print('------------------')
    print(find_empty_dir_paths(tree))

if __name__ == '__main__':
    main()
