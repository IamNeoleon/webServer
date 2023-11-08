
def split_Path_And_Param(path):
    data_url = path.split('?')
    return data_url if len(data_url) == 2 else [data_url[0], None]


def read_tampleate(path):
    content = ''
    with open(path, 'rb') as html_file:
        content = html_file.read().decode('utf-8')
    return content


def setParamTemp(data, **param):
    return data.format(**param)


def read_file(path_file):
    content = ''
    with open(path_file, 'rb') as file:
        content = file.read()
    return content