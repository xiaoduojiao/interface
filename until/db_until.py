import time

import pymysql


class DBUtil:

    def __init__(self,host,user,password,port=3306):
        self.connect = pymysql.Connect(
            host=host,
            port=port,
            user=user,
            password=password,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
    def select(self,sql):
        cursor = self.connect.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        self.connect.commit()# 提交事务，如果不提交下次查询，查不到新数据
        cursor.close()
        return data
    def update(self,sql):
        """
        insert、update、delete
        :param sql:
        :return:
        """
        cursor = self.connect.cursor()
        cursor.execute(sql)
        self.connect.commit()
        cursor.close()
    def close(self):
        if self.connect!=None:
            self.connect.close()

def wait_and_check_exist(db_util_cus,sql,timeout):
    '''等待查询结果返回，超时时间自定义'''
    start_time = time.time()
    print(sql)
    while len(db_util_cus.select(sql)) == 0:
        if time.time() - start_time >= timeout:
            print(f"超出等待时间:{sql}")
            return False
        time.sleep(1)  # 每次休眠 1 秒
    # print(f"查询成功")
    return db_util_cus.select(sql)

def wait_and_check_key(db_util_cus,sql,key,value,timeout):
    '''等待查询结果返回，超时时间自定义'''
    start_time = time.time()
    print(sql)
    while db_util_cus.select(sql)[0][key] != value:
        if time.time() - start_time >= timeout:
            print(f"超出等待时间:{sql}")
            return False
        time.sleep(1)  # 每次休眠 1 秒
    # print(f"查询成功")
    return db_util_cus.select(sql)

if __name__ == '__main__':
    # db_util = DBUtil(host='121.42.15.146',user='root',password='Testfan#123')
    # for i in range(5):
    #     time.sleep(10)
    #     res = db_util.select('select * from mtxshop_trade.es_order order by order_id desc limit 2')
    #     print(res)
    # db_util.close()
    from until.json_util import extract_json

    db_util = DBUtil(host='10.9.15.251', user='customer_rw', password='BkEN_V0_7TN_afz9Ryd')

    check_sql = f"select * from customer.t_customer_application_callback \
                         where json like '%1681449829%';"
    res = db_util.select(check_sql)
    print(res)
    code = extract_json(res,'$..code')
    print(code)
    db_util.close()