import pytest,os
import schedule
import time
import os
from apscheduler.schedulers.blocking import BlockingScheduler












if __name__ == '__main__':
    pytest.main(['--clean-alluredir', "./test_get_hot_product_sort.py",  "-s", '--alluredir', '../report/tmp'])  # -s打印输出
    os.system("allure serve ../report/tmp")