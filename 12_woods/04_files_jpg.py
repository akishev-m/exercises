#!/usr/bin/env python

from hexlet.fs import mkdir, mkfile, get_children, get_meta, is_file, get_name
import copy

def check(item):
    if is_file(item) and get_name(item).endswith('.jpg'):
        return True
    return False

def compress(pict):
    if check(pict):
        name = get_name(pict)
        new_meta = copy.deepcopy(get_meta(pict))
        if new_meta['size']:
            print(new_meta['size'])
            new_meta['size'] = new_meta['size']/2
            print(new_meta['size'])
        new_file = mkfile(name, new_meta)
        return new_file
    else:
        return pict


def compress_images(tree):
    children = get_children(tree)
    new_children = list(map(compress, children))
    new_meta = copy.deepcopy(get_meta(tree))
    new_tree = mkdir(get_name(tree), new_children, new_meta)
    return new_tree

def main():
    tree = mkdir(
            'my documents',
            [
                mkdir('test', []),
                mkfile('avatar.jpg', {'size': 100}),
                mkfile('photo.jpg', {'size': 150}),
                mkfile('test2', {'size': 200})
            ],
            {'hide': False}
        )

    tree2 = mkdir(
            'my documents',
            [
                mkdir('documents.jpg'),
                mkfile('avatar.jpg', {'size': 100}),
                mkfile('passport.jpg', {'size': 200}),
                mkfile('family.jpg', {'size': 150}),
                mkfile('addresses', {'size': 125}),
                mkdir('assets'),
            ],
            {'test': 'haha'},
            )
    print('---------------------')
    print(compress_images(tree2))
    print('^^^^^^^^^^^^^^^^^^^^')
#    print(half(compress_images(tree)))

if __name__ == '__main__':
    main()
