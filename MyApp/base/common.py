#!/usr/bin/python
# -*- coding:utf-8 -*-
import re



def validateEmail(email):
    # 校验邮箱格式方法
    if re.match("[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?",email) != None:
        return True
    else:
        return False
if __name__ == '__main__':
    # email = '123@qq.com'
    # a = validateEmail(email)
    import os
    cur = os.path.dirname(os.path.realpath(__file__))
    print(cur)
    file_path = os.path.join(cur, 'MyApp\static', 'git_1.png')
    print(file_path)