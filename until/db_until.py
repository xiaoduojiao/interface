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

if __name__ == '__main__':
    pass