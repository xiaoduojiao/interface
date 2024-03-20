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
    pass