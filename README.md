# RegressionAPP
- 自动化回归APP渠道包
- 通过uiautomator2支持WIFI或数据线连接
- APP安装包必须通过远程服务器，不支持本地安装

## 依赖：
```
# 1.下载Android Platform Tools（ADB工具）
国内地址：http://tools.android-studio.org/
翻墙地址：https://developer.android.com/studio/releases/platform-tools.html

# 2.包含adb.exe的目录加入到环境变量PATH中

# 3.安装uiautomator2（Android UI自动化框架，支持WIFI和USB两种连接方式）
git clone https://github.com/openatx/uiautomator2
pip install -e uiautomator2

# 4.安装pillow（图形处理库）
pip install pillow

# 5.打开手机的开发者选项中的USB调试，开始初始化
python -m uiautomator2 init

```

## 使用：
##### 1. 在脚本中配置手机IP或序列号
##### 2. 在脚本中配置 APP包名、下载路径以及渠道名
```
CONNECT_METHOD = '4d986a30'                       # 连接设备，也支持IP '192.168.1.166'
APP_NAME = 'com.xxx.yyy'
INSTALL_PATH = "http://10.40.4.200/bao/zzz_"      # 路径不能带中文
VERSION = '443'                                   # APP版本号
qudaos = ['aliyingyong', 'anzhuoshichang', 'baiduzhushou', 'dongfangrongziwang', 'huawei', 'm360zhushou',
              'm91zhushou', 'oppo', 'vivo', 'wandoujia', 'xiaomishangdian', 'yingyongbao']
```
##### 3. 上传渠道包至自己的测试服务器上的指定路径
##### 4. 开始执行脚本
```
python main.py

```

## 输出：
##### 1. 在output目录下生成首页的截图
##### 2. 在output目录下输出日志


## PS：
- 每次执行脚本会清理以前的截图和日志；
- 现在只校验了首页，可以简单的修改下，断言其他app内容；
- 暂时只写了oppo手机的权限校验；


