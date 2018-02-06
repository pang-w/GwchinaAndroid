#encoding=utf-8
import pymysql
from public import Log

log = Log.Logger(logger='SQLDataInfo').getLog()

def get_area_list():
    try:
        #charset='utf8' 解决中文乱码问题
        #创建连接
        conn = pymysql.connect('172.168.50.26','csall','111111','lssw',charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        #获取 com_device_state 表里的锁屏状态  locdek = 1 锁屏，locdek = 0 解屏
        #id = 948807 天机MINI 03
        #id = 948688 天机MINI 05
        cursor.execute("select value from com_param_device where name = 'rail_position' and bind_id = 1097963")
        lock = cursor.fetchall()
        #关闭游标、关闭数据库连接
        cursor.close()
        conn.close()
        return lock
    except:
        log.info('从数据库获取锁屏状态失败')
        print('连接SQL失败')

def get_user_set_update(value):
    try:
        #charset='utf8' 解决中文乱码问题
        #创建连接
        conn = pymysql.connect('172.168.50.26','csall','111111','lssw',charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        #获取 com_device_state 表里的锁屏状态  locdek = 1 锁屏，locdek = 0 解屏
        #id = 948807 天机MINI 03
        #id = 948688 天机MINI 05
        if value == 'lock_mute':
            cursor.execute("select param_value from com_user_param where user_id = 150478392 and param_name = 'lock_mute'")
        elif value == 'openpush':
            cursor.execute("select param_value from com_user_param where user_id = 150478392 and param_name = 'openpush'")
        elif value == 'opensms':
            cursor.execute("select param_value from com_user_param where user_id = 150478392 and param_name = 'opensms'")
        elif value == 'screenshotctrl':
            cursor.execute("select param_value from com_user_param where user_id = 150478392 and param_name = 'screenshotctrl'")
        elif value == 'system_message_notify':
            cursor.execute("select param_value from com_user_param where user_id = 150478392 and param_name = 'system_message_notify'")
        elif value == 'dynamic_message_notify':
            cursor.execute("select param_value from com_user_param where user_id = 150478392 and param_name = 'dynamic_message_notify'")

        lock = cursor.fetchall()
        #关闭游标、关闭数据库连接
        cursor.close()
        conn.close()
        return lock
    except:
        log.info('从数据库com_user_param获取lock_mute、screenshotctrl、system_message_notify、dynamic_message_notify出现错误')
        print('连接SQL失败')

def sql_url_limit_id():
    try:
        conn = pymysql.connect('172.168.50.26','csall','111111','lssw',charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        #获取 com_rule_url2 表里的 url_limit_id = 1 严格  2 标准 3 轻松
        cursor.execute("select url_limit_id from com_rule_url2 where bind_id = 1097963 AND active = 1")
        url_ids = cursor.fetchall()
        # sql_url_ids 为 （） 时，加上以下日志会返回None，print('连接SQL失败')
        # My_log.pyweblog().info('从SQL获取网址管理等级 %s ' % url_ids)
        cursor.close()
        conn.close()
        log.info('从SQL获取网址管理等级 %s ' % url_ids)
        return url_ids[0]

    except:
        log.info('从SQL获取网址管理等级失败')
        print('连接SQL失败')

def sql_url_black_white(type):
    try:
        conn = pymysql.connect('172.168.50.26','csall','111111','lssw',charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        #获取 com_rule_url 表里的 type_flag = 0 黑名单 = 1 白名单
        if type == 0:
            cursor.execute("select url_domain from com_rule_url where bind_id = 1097963 AND type_flag = 0 AND active = 1")
            black_list = cursor.fetchall()
            cursor.close()
            conn.close()
            log.info('从SQL获取网址黑名单网址list为  %s ' % black_list)
            # for black in range(len(black_list)):
            #     return black
            return black_list
        elif type == 1:
            cursor.execute("select url_domain from com_rule_url where bind_id = 1097963 AND type_flag = 1 AND active = 1")
            white_list = cursor.fetchall()
            cursor.close()
            conn.close()
            log.info('从SQL获取网址白名单网址list为  %s ' % white_list)
            return white_list

    except:
        log.info('从SQL获取网址黑、白名单网址失败')
        print('None')

def sql_url_key():
    try:
        conn = pymysql.connect('172.168.50.26','csall','111111','lssw',charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        #获取 com_rule_keyword 表里的 active = 1 逻辑删除 1 未删除 0 已删除，但仍然保存在数据库
        cursor.execute("select keyword from com_rule_keyword where bind_id = 1097963 and active = 1")

        # cursor.fetchone()   取一条数据  cursor.fetchall()取满足条件的所有数据
        # row_1 = cursor.fetchone()
        url_key = cursor.fetchall()
        # 当url_key 为 （） 时，加上以下日志会返回None，print('连接SQL失败')
        # My_log.pyweblog().info('从SQL获取网址关键字 %s ' % url_key)
        cursor.close()
        conn.close()
        return url_key
    except:
        log.info('从SQL获取网址关键字失败')
        print('连接SQL失败')

def sql_switch_key():
    '''获取切换网址管理 - 关键字 - 系统关键字的开关值  offline_keyword_shielding  0 - 关  1 - 开'''
    '''
    "select `value` from com_param_device where bind_id = 1097963 and `name` = 'offline_keyword_shielding'"
    value、name 作为sql 关键字，查询时需加上 ` ` （1左边的符号）,查看字符类型值需加上 ' '
    '''
    try:
        conn = pymysql.connect('172.168.50.26','csall','111111','lssw',charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        #获取 com_rule_url2 表里的 url_limit_id = 1 严格  2 标准 3 轻松
        cursor.execute("select `value` from com_param_device where bind_id = 1097963 and `name` = 'offline_keyword_shielding'")
        sql_switch_key = cursor.fetchone()
        # sql_url 为 （） 时，加上以下日志会返回None，print('连接SQL失败')
        # My_log.pyweblog().info('从SQL获取黑、白名单网址 %s ' % url)
        cursor.close()
        conn.close()
        return sql_switch_key
    except:
        log.info('从SQL获取黑、白名单网址失败')
        # print('连接SQL失败')

def sql_locked():
    '''获取锁屏状态的值'''
    try:
        #charset='utf8' 解决中文乱码问题
        #创建连接
        conn = pymysql.connect('172.168.50.26','csall','111111','lssw',charset='utf8')
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        #获取 com_device_state 表里的锁屏状态  locdek = 1 锁屏，locdek = 0 解屏
        cursor.execute("select locked from com_device_state where bind_id = 1097963")

        lock = cursor.fetchone()
        log.info("从SQL获取锁屏状态'1 == 锁屏， 0 == 解屏' %s " % lock)

        #关闭游标、关闭数据库连接
        cursor.close()
        conn.close()
        return lock['locked']
    except:
        log.info('从数据库获取锁屏状态失败')
        print('连接SQL失败')

if __name__  == '__main__':
    x = sql_locked()
    print(x)
    print(type(x))


