#!/usr/bin/env python

import copy
from hexlet.fs import mkdir, mkfile, get_children, get_meta, is_file, get_name


def downcase_file_names(node):
    name = get_name(node)
    new_meta = copy.deepcopy(get_meta(node))
    if is_file(node):
        return mkfile(name.lower(), new_meta)
    children = get_children(node)
    new_children = list(map(lambda child: downcase_file_names(child), children))
    new_tree = mkdir(name, new_children, new_meta)
    return new_tree

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
    print(tree)
    new_tree = downcase_file_names(tree)
    new_file = get_children(new_tree)[1]
    get_name(new_file)
    print('------------------')
    print(new_tree)

if __name__ == '__main__':
    main()
