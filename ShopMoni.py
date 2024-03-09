ShopList = {}
OrderList = []


def ShowMenu():
    print("----------------菜单---------------")
    print("|             1.添加商品           |")
    print("|             2.删除商品           |")
    print("|             0.退出应用           |")
    print("----------------------------------")


def FuncSplit(item):
    begin = 0
    end = len(item) - 1
    ObjectList = []
    while True:
        mid = begin + (end - begin) // 2
        if item[mid].isnumeric() is True and item[mid + 1].isnumeric() is False:
            result = mid
            break
        elif item[mid].isnumeric() is True and item[mid + 1].isnumeric() is True:
            begin = mid
        elif item[mid].isnumeric() is False:
            end = mid
    ObjectList.append(item[0:result + 1])
    ObjectList.append(item[result + 1:])
    return ObjectList


def ShopInit():
    global ShopList
    item = input("请输入商品编号和商品名称：")
    ObjectList = FuncSplit(item)
    ShopList[ObjectList[0]] = ObjectList[1]


def FuncShow():
    global ShopList
    print("库存商品如下：")
    for key, value in ShopList.items():
        print(str(key) + "-->" + value)


def OrderShow():
    global OrderList
    print("你的购物车如下：")
    print("序列 | 编号 | 物品")
    idx = 1
    for itembox in OrderList:
        print(str(idx) + " | " + str(itembox[0]) + " | " + str(itembox[1]))
        idx += 1


def AddOrder():
    global OrderList, ShopList
    FuncShow()
    i = input("请输入需要添加商品的编号(返回请按q)：")
    while i != "q" and i != "Q":
        if ShopList.get(i) is None:
            print("该商品不存在！")
        else:
            OrderList.append((int(i), ShopList[i]))
            OrderShow()
        i = input("请输入需要添加商品的编号(返回请按q)：")


def PopOrder():
    global OrderList, ShopList
    OrderShow()
    i = input("请输入需要删除商品的序号(返回请按q)：")
    while i != "q" and i != "Q":
        if int(i) <= 0 or int(i) > len(OrderList):
            print("该序号超出范围，请重新输入！")
        else:
            OrderList.remove(OrderList[int(i) - 1])
            OrderShow()
        i = input("请输入需要删除商品的序号(返回请按q)：")


def MainFunc():
    qal = int(input("请输入需要上架的商品数量："))
    while qal > 0:
        ShopInit()
        qal -= 1
    while True:
        ShowMenu()
        num = input("请输入对应编号：")
        if int(num) == 1:
            AddOrder()
        elif int(num) == 2:
            PopOrder()
        elif int(num) == 0:
            break
        else:
            print("该选项非法，请重新输入！")
        num = input("请输入对应编号：")


MainFunc()
