import time

import pymysql

def wait_and_check(func):
    '''等待查询结果:超时时间自定义'''
    def wrapper(*args,**kwargs):
        try:
            if kwargs.get('key') and kwargs.get('value') and kwargs.get('timeout'):
                start = time.time()
                result = func(*args, **kwargs)
                while result[0][kwargs.get('key')] != kwargs.get('value'):
                    if time.time() - start > kwargs['timeout']:
                        print(f"查询超时，未查询到结果，期望为{kwargs.get('value')}，实际为{result[0][kwargs.get('key')] }:{kwargs.get('sql')}")
                        break
                    time.sleep(1)
            elif kwargs.get('timeout') is not None:
                start = time.time()
                result = func(*args,**kwargs)
                while len(result) == 0:
                    if time.time() - start > kwargs['timeout']:
                        print(f"查询超时，未查询到结果:{kwargs.get('sql')}")
                        break
                    time.sleep(1)
            return func(*args, **kwargs)
        except Exception as e:
            return func(*args,**kwargs)
    return wrapper

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

    @wait_and_check
    def select(self, sql,timeout=1,key=None,value=None):
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

if __name__ == '__main__':
    db_util = DBUtil(host='xxx', user='xxx', password='xxx')
    re = db_util.select(sql = "select * from xxx.xxx limit 1;",key='id',value=2,timeout=3)
    print(re)