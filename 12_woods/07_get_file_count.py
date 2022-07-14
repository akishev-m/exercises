#!/usr/bin/env python

import copy
from hexlet.fs import mkdir, mkfile, get_children, get_meta, is_file, get_name, is_directory


def get_files_count(node):
    if is_file(node):
        return 1
    children = get_children(node)
    descendant_counts = list(map(get_files_count, children))
    return sum(descendant_counts)


def get_subdirectories_info(node):
    children = get_children(node)
    filtered = filter(is_directory, children)
    result = map(
            lambda child: (get_name(child), get_files_count(child)),
            filtered,
            )
    return list(result)

def main():
    tree = mkdir('/', [
        mkdir('etc', [
            mkdir('apache'),
            mkdir('nginx', [
                mkfile('.nginx.conf'),
            ]),
        ]),
         mkdir('.consul', [
            mkfile('.config.json'),
            mkfile('file.tmp'),
            mkfile('data'),
         ]),
        mkfile('hosts'),
        mkfile('resolve'),
    ])
    print((tree))
    print('------------------')
    print(get_subdirectories_info(tree))

if __name__ == '__main__':
    main()
