import json
import os
import re
import sys
from base64 import urlsafe_b64decode


class ssr_link_d(object):
    def __init__(self, file_name):
        self._file_name = file_name
        self.server_list = [i for i in self.info.keys()]

    @property
    def info(self):
        _info = dict()
        with open(self._file_name, 'r') as f:
            pre_str = urlsafe_b64decode(f.read() +
                                        '==').decode('utf-8').split('\n')
            pre_str = [i[6:] for i in pre_str]
            pre_str = [i for i in filter(None, pre_str)]
            for b64d in pre_str:
                one_str = re.split(
                    '=|&|[\/?]|:',
                    urlsafe_b64decode(b64d + '==').decode('utf-8'))
                one_str = [i for i in filter(None, one_str)]
                for num, i in enumerate(one_str):
                    try:
                        one_str[num] = urlsafe_b64decode(i +
                                                         '==').decode('utf-8')
                    except Exception:
                        continue
                    _info[one_str[0]] = one_str
            return _info

    @property
    def conf(self):
        _conf = self.info[self.server_list[0]]
        ssr_conf = dict()
        ssr_conf['server'] = _conf[0]
        ssr_conf['local_address'] = '0.0.0.0'
        ssr_conf['local_port'] = 8089
        ssr_conf['timeout'] = 300
        ssr_conf['workers'] = 1
        ssr_conf['server_port'] = _conf[1]
        ssr_conf['password'] = _conf[5]
        ssr_conf['method'] = _conf[3]
        ssr_conf['obfs'] = _conf[4]
        ssr_conf['obfs_param'] = _conf[7]
        ssr_conf['protocol'] = _conf[2]
        ssr_conf['protocol_param'] = _conf[9]
        return ssr_conf


def main():
    args = sys.argv[1:]
    if '-h' in args or '--help' in args:
        print('help')
    else:
        if args.count('-c'):
            s = ssr_link_d(args[args.count('-c')])
            if not args.count('-P'):
                print(s.server_list)


if __name__ == '__main__':
    main()
