import re
import uuid


def generate_random_string(length):
    """
    生成随机字符串
    :param length: 输入字符串的长度
    :return: 返回随机字符串
    """
    random_string = str(uuid.uuid4())[:length]
    return random_string


def show_menu():
    """
    展示菜单
    :return: 无返回
    """
    print("-" * 50)
    print('|''{0:^46}'.format('1.匹配数字') + '|')
    print('|''{0:^46}'.format('2.匹配字母') + '|')
    print('|''{0:^45}'.format('3.匹配数字字母') + '|')
    print("-" * 50)


def match_string(string, mode):
    """
    匹配随机字符串
    :param string: 需匹配的字符串
    :param mode: 匹配模式
    :return: 返回匹配结果
    """
    if mode == 1:
        pattern = '\d+'
    elif mode == 2:
        pattern = '[A-Za-z]+'
    elif mode == 3:
        pattern = '[A-Za-z0-9]+'
    match = re.findall(pattern, string)
    if match is None:
        result = "无匹配"
    else:
        result = match
    return result


def main():
    length = int(input("请输入随机字符串长度："))
    while 0 < length <= 50:
        string = generate_random_string(length)
        print(f"随机字符串为：{string}")
        show_menu()
        while True:
            mode = int(input("请输入匹配模式："))
            if mode <= 0 or mode > 3:
                print("输入数字过小或过大!")
            else:
                break
        result = match_string(string, mode)
        print(result)
        length = int(input("请输入随机字符串长度："))


main()
