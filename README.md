# GetTagIdPyQt
* https://github.com/liuduokai/GetTagMAC的图形化实现
* 根据获取到的UWB基站的定位标签的MAC信息统计检测到的标签数量，同时显示标签的ID。使用PyQt实现了图形化界面

## 文件
* callMainWindow.py:调用界面布局文件生成界面
* callMainWindow.spec:使用pyinstaller生成exe程序的配置文件
* con_oracle.py:数据库连接文件，使用oracle数据库
* fuc.py:功能实现文件
* main.py:界面布局文件
* main.ui:qtdesigner生成的xml文件

## 开发中遇到的问题

### 1. 图形界面无法实时同步
* 后经查询资料发现问题出在，当使用异步函数的事件循环监听事件时会阻塞QT主循环的运行，后使用asyncio+多线程解决
* https://blog.csdn.net/qq_27825451/article/details/86483493

### 2.数据库连接问题
* 经实验后连接oracle必须的两个dll文件为oraociei11.dll和oci.dll
* 打包时需要将dll文件置于文件根目录下
* 数据库的连接配置使用ini文件，打包过后的程序运行也需要在程序目录下放置ini配置文件