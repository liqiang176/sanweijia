import yaml

def get_yaml_data(fileDir):
    resultList = []
    #1.读取文件
    f = open(fileDir,'r',encoding='utf-8')
    #2.使用yaml获取数据
    res = yaml.load(f,Loader=yaml.FullLoader)
    info = res[0]
    del  res[0]
    for one in res:
        resultList.append((one['data'],one['resp']))
    f.close()
    return resultList


if __name__ == '__main__':
    res = get_yaml_data('../data/get_hot_product_sort.yaml')