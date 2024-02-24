import json
import os
import time

import requests
from pyquery import PyQuery as pq

from header.writeheaders import header


def request(baseurl: str, param: list, headers: dict) -> None:
    """
    发送请求
    :param baseurl: 基础地址
    :param param: 参数
    :param headers: 请求头
    :return: None
    """
    os.mkdir('./result/content')
    txt_code = ''
    for i in range(len(param)):
        res = requests.get(baseurl + str(param[i]), headers=headers)
        txt = res.text
        code = res.encoding
        txt_code = code
        with open(f'./result/content/{i + 1}页.txt', 'w', encoding=code) as f:
            f.write(txt)
        print(f'完成第{i + 1}个请求')
        time.sleep(2)  # 防止频繁请求导致爬取失败
    with open('./result/code.txt', 'w') as f:
        f.write(txt_code)


def readData(NumberOfPages: int, startline: int, endline: int, code):
    """
    读取响应，保留文本
    :param NumberOfPages: 页数
    :param startline: 保留行的开头
    :param endline: 保留行的结尾
    :return: None
    """
    for i in range(NumberOfPages):
        with open(f'result/content/{i + 1}页.txt', 'r', encoding=code) as f:
            txt = f.readlines()[startline - 1:endline - 1]
            with open(f'result/content/{i + 1}页.txt', 'w', encoding=code) as f:
                f.writelines(txt)
            print(f"第{i + 1}个响应处理完毕")


def solveData(NumberOfPages, code) -> dict:
    """
    整理文本数据
    :param NumberOfPages: 页数
    :param code: 编码
    :return: 处理好的数据
    """
    result = {}
    for k in range(NumberOfPages):
        with open(f'result/content/{k + 1}页.txt', 'r', encoding=code) as f:
            # 处理文本,将文本变成大字符串
            html = ''
            for item in f.readlines():
                html += item
            content = pq(html)
            
            lst = []
            dic = {}
            # 处理字符串中的特殊字符
            for item in content(".info").items():
                lst.append(list(item.text().replace('\xa0', '').split('\n')))
            # 提取文本
            key = ["title", "performer", "year", "score", "quote"]
            for i in range(len(lst)):
                info = {}
                for j in range(len(lst[i])):
                    if j == 0:
                        # 去掉【可播放】
                        info[key[j]] = lst[i][j][0:len(lst[i][j]) - 5]
                    else:
                        info[key[j]] = lst[i][j]
                dic[f"第{str(i + 1)}个"] = info
            result[f"第{str(k + 1)}页"] = dic
    return result


def saveData(path: str, dic: dict):
    # ensure_ascii=False参数告诉函数不要将非ASCII字符转义为\uXXXX序列
    with open(path, 'w', encoding='utf-8') as f:
        txt = json.dumps(dic, ensure_ascii=False)
        f.write(txt)
    print('项目完成，请查看')


def main():
    os.mkdir('./result')
    
    baseurl = 'https://movie.douban.com/top250?start='
    param = [str(i * 25) for i in range(10)]
    headers = header()
    # 请求数据
    request(baseurl, param, headers)
    with open('./result/code.txt', 'r') as f:
        code = f.read()
    # 读取数据
    readData(10, 302, 1299, code)
    
    # 处理数据
    dic = solveData(10, code)
    
    # 保存数据json
    saveData('./result/data.json', dic)


main()
