#!/usr/bin/env python


READ_ONLY = 'read_only'

def toggle(flag, st):
    if flag in st:
        st.discard(flag)
    else:
        st.add(flag)

def toggled(flag, st):
    new_set = set(st)
    new_set.add(flag)
    return new_set




def main():
    f = READ_ONLY
    fls = {1, 5, 'kj'}
    toggle(f, fls)
    print(f in fls)
    toggle(f, fls)
    print(f in fls)
    new_flags = toggled(f, fls)
    print(f in fls)
    print(f in new_flags)

    

if __name__ == '__main__':
    main()
