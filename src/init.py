# -*- coding: utf-8 -*-

import sys


def main(title: str):

    with open('src/{}.py'.format(title), 'w') as f:
        f.write('# -*- coding: utf-8 -*-\n\nif __name__ == \'__main__\':\n    print(\'x\')\n')

    with open('tests/test_{}.py'.format(title), 'w') as f:
        f.write('# -*- coding: utf-8 -*-\n\nfrom src.{} import *\n'.format(title))


if __name__ == '__main__':
    args = sys.argv
    if (len(args) < 2):
        print('[ERROR] Title parameter is required')
        sys.exit(2)
    main(args[1])
