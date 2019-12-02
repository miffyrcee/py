import yaml

with open('/home/miffyrcee/github/conf/config.yaml', 'r') as fr:
    table_list = yaml.load(fr, Loader=yaml.FullLoader)
    print(table_list)
    sort_file = yaml.dump(table_list, sort_keys=True)
    sort_file[1]
    print(sort_file)
