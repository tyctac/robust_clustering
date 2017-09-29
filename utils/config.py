#encoding=utf8
import yaml

def get_home_dir():
    # f = open('../utils/config.yaml')
    # f = open('../utils/config.yaml')
    f = open('/home/zw/Documents/project/Clustering/utils/config.yaml')
    x = yaml.load(f)
    f.close()
    return x['HOME_DIR']

def get_title_weight():
    f = open('/home/zw/Documents/project/Clustering/utils/config.yaml')
    x = yaml.load(f)
    f.close()
    return x['TITLE_WEIGHT']

def get_reg_person_weight():
    f = open('/home/zw/Documents/project/Clustering/utils/config.yaml')
    x = yaml.load(f)
    return x['REG_PERSON_WEIGHT']

def get_time_limit():
    f = open('/home/zw/Documents/project/Clustering/utils/config.yaml')
    x = yaml.load(f)
    print type(x['TIME_LIMIT'])
    return x['TIME_LIMIT']

def main():
    x =  get_home_dir()
    print x


if __name__ == '__main__':
    main()