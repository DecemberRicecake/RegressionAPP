# -*- encoding=utf8 -*-
import logging
import os
import uiautomator2 as u2
from time import sleep

CONNECT_METHOD = '4d986a30'                       # 连接设备，也支持IP '192.168.1.166'
APP_NAME = 'com.xxx.yyy'
INSTALL_PATH = "http://10.40.4.200/bao/zzz_"      # 路径不能带中文
VERSION = '443'                                   # APP版本号
qudaos = ['aliyingyong', 'anzhuoshichang', 'baiduzhushou', 'dongfangrongziwang', 'huawei', 'm360zhushou',
              'm91zhushou', 'oppo', 'vivo', 'wandoujia', 'xiaomishangdian', 'yingyongbao']


def oppo_verify(u):
    """ 处理oppo权限问题 """
    if u(packageName="com.coloros.safecenter", textContains="需要您验证身份后安装").exists:
        u.set_fastinput_ime()
        u(className='android.widget.EditText').set_text('123456')
        u(className='android.widget.Button', text='安装').click()
    if u(packageName="com.android.packageinstaller", resourceId="com.android.packageinstaller:id/bottom_button_layout").exists:
        u.click(0.714, 0.96)
        return True


def install_bao(url):
    """ 安装apk """
    u.app_uninstall(APP_NAME)
    u.app_install(url, installing_callback=oppo_verify)
    # u(resourceId="com.android.packageinstaller:id/bottom_button_two").click()
    logger.info('apk installed over!!!')


def del_file(path):
    """ 删除目录中的文件 """
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path, i)
        if os.path.isdir(c_path):
            del_file(c_path)
        else:
            os.remove(c_path)


def init_file():
    """ 初始化 """
    if os.path.exists('./output'):
        del_file('./output')
    else:
        os.mkdir('./output')


def get_screen(qudao):
    """ 截图并保存 """
    u.screenshot("./output/"+qudao+".jpg")
    logger.info('end test qudaobao: '+qudao)


def app_login():
    """ 登录APP """
    # u.app_clear(APP_NAME)
    u.app_start(APP_NAME)
    u(resourceId=APP_NAME+":id/guide_Login").click()
    # u(resourceId=APP_NAME + ":id/" + "main_tab_user_name").click()
    # u(resourceId=APP_NAME + ":id/" + "btn_tab_fragment_user_login_register").click()
    u(resourceId=APP_NAME + ":id/" + "user_phone").send_keys("13912345678")
    u(resourceId=APP_NAME + ":id/" + "user_pwd").send_keys("Aa123456")
    u(resourceId=APP_NAME + ":id/" + "login").click()
    logger.info('login over!')


def loggers():
    """ 日志管理 """
    log = logging.getLogger('mewlogger')
    log.setLevel(logging.DEBUG)
    fh = logging.FileHandler('./output/test.log')  # 日志文件
    ch = logging.StreamHandler()
    # fh.setLevel(logging.DEBUG)
    formatter = logging.Formatter('[%(asctime)s][%(thread)d][%(filename)s][%(levelname)s] ### %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    log.addHandler(fh)                  # 给log添加handler
    log.addHandler(ch)
    return log


def main():
    for qudao in qudaos:
        logger.info('start test qudaobao: ' + qudao)
        url = INSTALL_PATH + qudao + '_' + VERSION + '.apk'
        try:
            print(url)
            install_bao(url)                # 安装apk
            app_login()                     # 登录融管家
            sleep(5)                        # 首页数据加载比较慢，等待5秒
            get_screen(qudao)               # 截图
        except:
            logger.error('find exception： '+qudao)
            sleep(5)
            continue


if __name__ == '__main__':
    init_file()  # 初始化
    logger = loggers()                  # 开启日志
    logger.info('connect phone...')
    u = u2.connect(CONNECT_METHOD)      # 连接
    # u.open_identify()
    # print(u.info)
    main()
    logger.info('all qudaobao test over!')



