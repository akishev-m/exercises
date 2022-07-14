#!/usr/bin/env python

import copy
from hexlet.fs import mkdir, mkfile, get_children, get_meta, is_file, get_name


def change_owner(node, owner):
    name = get_name(node)
    new_meta = copy.deepcopy(get_meta(node))
    new_meta['owner'] = owner
    if is_file(node):
        return mkfile(name, new_meta)
    children = get_children(node)
    new_children = list(map(lambda child: change_owner(child, owner), children))
    new_tree = mkdir(name, new_children, new_meta)
    return new_tree


