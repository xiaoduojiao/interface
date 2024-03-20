import time
from random import randint

from faker import Faker

fake = Faker(locale='zh_CN')

def rdm_street_address():
    return fake.street_address()

def rdm_phone_number():
    return fake.phone_number()

def cur_timestamp():#到毫秒级的时间戳
    return int(time.time() * 1000)

def cur_date():# 2021-12-25
    return fake.date_between_dates()

def cur_date_time():# 2021-12-25 10:07:33
    return fake.date_time_between_dates()

def rdm_date(pattern='%Y-%m-%d'):
    return fake.date(pattern=pattern)

def rdm_date_time():
    return fake.date_time()

def rdm_name():
    return fake.name()

def rdm_company():
    return fake.company()


# 将整数随机拆分成n个整数
def SplitNum(split_num, num):
    '''
    split_num 拆分个数
    num 被拆分的整数
    '''
    rand_ls = [randint(1, 10) for _ in range(split_num)]
    rand_sum = sum(rand_ls)
    p = list(map(lambda i: int(i/rand_sum * num), rand_ls))
    p[-1] = num - sum(p[0:split_num-1])
    return p



if __name__ == '__main__':
    print(rdm_phone_number())
    # print(rdm_date())
    # print(rdm_date_time())
    # print(cur_date())
    # print(cur_timestamp())
    # print(cur_date_time())
    print(rdm_name())
    # print(SplitNum(82, 133215780))
