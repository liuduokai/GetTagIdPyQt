import cx_Oracle as cx
from configparser import ConfigParser


# 连接数据库模块
def get_tag_id(mac_id):

    cfg = ConfigParser()
    cfg.read('config.ini')

    ip = cfg.get('DB', 'ip')
    port = cfg.get('DB', 'port')
    db = cfg.get('DB', 'db')
    username = cfg.get('DB', 'username')
    pwd = cfg.get('DB', 'pwd')

    dsn = cx.makedsn(ip, port, db)
    try:
        connection = cx.connect(username, pwd, dsn)
    except OSError as err:
        print(err)
        print('连接错误')
    cursor = connection.cursor()
    print("数据库连接成功")
    sql = "SELECT BLUETOOTHID FROM UWB_T_UWBTAGS where UWBTAGID = " + str(mac_id)
    cursor.execute(sql)
    data = cursor.fetchone()  # 获取一条数据
    print("获取数据成功")
    # print(type(data))
    if data:
        return data[0]
    else:
        return '未定义'



if __name__ == '__main__':

    cfg = ConfigParser()
    cfg.read('config.ini')

    ip = cfg.get('DB', 'ip')
    port = cfg.get('DB', 'port')
    db = cfg.get('DB', 'db')
    username = cfg.get('DB', 'username')
    pwd = cfg.get('DB', 'pwd')

    print(ip, port, db, username, pwd)

    dsn = cx.makedsn(ip, port, db)
    connection = cx.connect(username, pwd, dsn)

    print("oracle版本：", connection.version)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM UWB_T_UWBTAGS")

    datas = cursor.fetchone()  # 获取一条数据
    datas = cursor.fetchall()

    for data in datas:
        print(data)

    cursor.close()
    connection.close()

# con = cx.connect('test_db', 'pwd', '127.0.0.1:1521/ORCL')
# # 创建游标
# cursor = con.cursor()
# # 执行命令，该命令是查看该数据库中所有表的名字
# cursor.execute("SELECT table_name FROM user_tables")
# # datas = cursor.fetchone()        #获取一条数据
# datas = cursor.fetchall()
# # 输出数据
# print(datas)
#
# # 关闭连接
# cursor.close()
# con.close()
