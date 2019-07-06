import base64
import json
import re
from base64 import urlsafe_b64decode

path = '/home/miffyrcee/Downloads/0Lh2CI1udDX9hKTn.txt'


def gen_pre(path):
    with open(path, 'r') as f:
        pre_str = urlsafe_b64decode(f.read()).decode('utf-8').split('\n')
        pre_str = [i[6:] for i in pre_str]
        pre_str = [i for i in filter(None, pre_str)]
        return pre_str


def gen_one(pre_str):
    one_str = re.split(':|[\/?]|=|&',
                       urlsafe_b64decode(pre_str + '==').decode('utf-8'))
    one_str = [i for i in filter(None, one_str)]
    print(one_str)
    for num, i in enumerate(one_str):
        try:
            one_str[num] = urlsafe_b64decode(i + '==').decode('utf-8')
        except Exception:
            continue
    return one_str


def gen_conf(one_str):
    ssr_conf = dict()
    ssr_conf['server'] = one_str[0]
    ssr_conf['local_address'] = '0.0.0.0'
    ssr_conf['local_port'] = 8089
    ssr_conf['timeout'] = 300
    ssr_conf['workers'] = 1
    ssr_conf['server_port'] = one_str[1]
    ssr_conf['password'] = one_str[5]
    ssr_conf['method'] = one_str[3]
    ssr_conf['obfs'] = one_str[4]
    ssr_conf['obfs_param'] = one_str[7]
    ssr_conf['protocol'] = one_str[2]
    ssr_conf['protocol_param'] = one_str[9]
    return ssr_conf


def gen_server_name():
    print(gen_one(gen_pre(path)[0]))
    print(urlsafe_b64decode('ZG93bmxvYWQud2luZG93c3VwZGF0ZS5jb20=='))


def main():
    gen_server_name()
if __name__ == '__main__':
    main()
