# 1
# 2
# 3
'''
1
2
3
4
5
6
7
8
9
0
11
12
13
14
15
'''






























import os
import sys
import scipy
import datetime
import time
def test():
    if True:
        print(sys)
        print(time)
        print(len(time.time))
    else:
        print(sys)
        print(time)
        print(len(time.time))
    for i in range(100):
        if i % 10==0:
            print(sys)
            print(time)
            print(len(time.time))
        elif i % 9 == 0:
            print(sys)
            print(time)
            print(len(time.time))
        elif i % 8 == 0:
            print(sys)
            print(time)
            print(len(time.time))

def get_commit_diff_comment_rows(filepath, diff):
    endfix = filepath.split("/")[-1].split('.')[-1]
    diff_rows = diff.split("\n")
    if len(diff_rows) < 3:
        return {}
    luanges = {
        'py': {
            'single': '#',
            'multi_start': ["'''", '"""'],
            'multi_end': ["'''", '"""']
        },
        'java': {
            'single': '//',
            'multi_start': ["/*"],
            'multi_end': ["*/"],
        },
        'js': {
            'single': '//',
            'multi_start': ["/*"],
            'multi_end': ["*/"],
        },
        'vue': {
            'single': '//',
            'multi_start': ["<!--", '/*'],
            'multi_end': ["-->", "*/"],
        },
        'html': {
            'single': '//',
            'multi_start': ["<!--", '/*'],
            'multi_end': ["-->", "*/"],
        },
        'jsx': {
            'multi_start': ["/*", "{/*"],
            'multi_end': ["*/", "*/}"],
        },
        'less': {
            'single': '//',
            'multi_start': ["/*"],
            'multi_end': ["*/"],
        },
        'rb': {
            'single': '#',
            'multi_start': ["=begin"],
            'multi_end': ["=end"],
        },
        'yml': {
            'single': '#',
        },

        'xml': {
            'multi_start': ["<!--"],
            'multi_end': ["-->"],
        },
        'sql': {
            'single': '--',
            'multi_start': ["/*"],
            'multi_end': ["*/"],
        },
        'sh': {
            'single': '#',
        },
        'css': {
            'multi_start': ["/*"],
            'multi_end': ["*/"],
        },
    }
    luange = luanges.get(endfix)
    if not luange:
        return {}
    single_start = luange.get("single")
    multi_start = luange.get("multi_start")
    multi_end = luange.get("multi_end")
    comment_add = 0
    comment_del = 0
    empty_add = 0
    empty_del = 0
    block_comment_flag = False  # 块注释默认为空
    for row in diff_rows:
        if row.startswith("---") or row.startswith("+++") or row.startswith("@@"):
            continue
        if row.startswith("+"):
            node_type = '+'
        elif row.startswith("-"):
            node_type = '-'
        else:
            continue
        row = row[1:].strip()
'''
1
2
3
4
5
6
7
8
9
0
11
12
13
14
15
16
17
18
'''