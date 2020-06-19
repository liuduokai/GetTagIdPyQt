import logging
import sys
import threading
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QDir, QProcess
from main import Ui_Form
import fuc
import con_oracle

import asyncio
import websockets


# 获取标签电量信息
def get_battery_info(message):
    m_hex = message.hex()
    battery_hex = m_hex[32:34]
    battery_dec = int(battery_hex, 16)
    return battery_dec


# 获取输出版本的MAC
def get_print_version_mac(message):
    m_hex = message.hex()
    tag_id_p_rev = m_hex[16:28]
    i = 5
    tag_id_p = ''
    while i >= 0:
        tag_id_p += tag_id_p_rev[(2 * i):(2 * i + 2)]

        if i != 0:
            tag_id_p += ':'

        tag_id_p = tag_id_p.upper()
        i -= 1
    return tag_id_p


# 主循环函数
async def consumer_handler(myWin):
    async with websockets.connect('ws://10.44.68.179:6432/ws', ping_interval=None) as websocket:
        async for message in websocket:
            try:
                tag_mac_p = get_print_version_mac(message)
            except OSError as err:
                logging.error("获取格式化MAC出错")
                logging.error(message)
                logging.error(tag_mac_p)

            # 获取数字版本MAC
            try:
                tag_mac = fuc.get_tag_mac(message)
            except OSError as err:
                logging.error("获取mac id出现错误")
                logging.error(err)
                logging.error(message)
                logging.error(tag_mac)

            # 获取电量信息
            try:
                tag_battery_info = get_battery_info(message)
            except OSError as err:
                logging.error("获取battery info出现错误")
                logging.error(err)
                logging.error(message)
                logging.error(tag_mac)

            # 是否是新检测到的标签
            if tag_mac_p in tag_mac_dict:
                tag_mac_dict[tag_mac_p] = tag_battery_info
            else:
                tag_mac_dict[tag_mac_p] = tag_battery_info
                myWin.addtext('********检测到新的标签********')
                myWin.addtext('编号:'+str(len(tag_mac_dict)))
                myWin.addtext('tag MAC:' + tag_mac_p)
                print(1)
                myWin.addtext('剩余电量：'+str(tag_battery_info)+'%')
                print(2)
                # 查询MAC对应的TAG ID
                try:
                    # print(tag_mac)
                    tag_id = con_oracle.get_tag_id(tag_mac)
                except OSError as err:
                    logging.error("获取tag id出现错误")
                    logging.error(err)
                    logging.error(message)
                    logging.error(tag_mac)
                    logging.error(tag_id)
                # print(mac_id)
                myWin.addtext('tag_id:' + tag_id)
                myWin.addtext('---------------------------')
                myWin.lcdNumber.display(str(len(tag_mac_dict)))


class MyMainForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.CloseButton.clicked.connect(self.close)
        self.ResetButton.clicked.connect(self.restart)

    def restart(self):
        program = QApplication.applicationFilePath()
        # print(program)
        arguments = QApplication.arguments()
        # print(arguments)
        workingDirectory = QDir.currentPath()
        # print(workingDirectory)
        QProcess.startDetached(program, arguments, workingDirectory)
        # QProcess.startDetached(program)
        self.close()

    def addtext(self, text):
        self.listWidget.addItem(text)
        self.listWidget.setCurrentRow(self.listWidget.count()-1)


def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


def main(myWin):
    coroutine1 = consumer_handler(myWin)
    new_loop = asyncio.new_event_loop()  # 在当前线程下创建时间循环，（未启用），在start_loop里面启动它
    t = threading.Thread(target=start_loop, args=(new_loop,))  # 通过当前线程开启新的线程去启动事件循环
    t.start()
    asyncio.run_coroutine_threadsafe(coroutine1, new_loop)  # 这几个是关键，代表在新线程中事件循环不断“游走”执行


if __name__ == "__main__":
    tag_mac_dict = dict()
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    main(myWin)
    sys.exit(app.exec_())
