import pymysql
from twisted.enterprise import adbapi
from scrapy.utils.project import get_project_settings  #导入seetings配置
import time


class DBHelper():
    '''这个类也是读取settings中的配置，自行修改代码进行操作'''

    def __init__(self):
        settings = get_project_settings()  #获取settings配置，设置需要的信息

        dbparams = dict(
            host=settings['MYSQL_HOST'],  #读取settings中的配置
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            charset='utf8',  #编码要加上，否则可能出现中文乱码问题
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=False,
        )
        #**表示将字典扩展为关键字参数,相当于host=xxx,db=yyy....
        dbpool = adbapi.ConnectionPool('pymysql', **dbparams)

        self.dbpool = dbpool

    def connect(self):
        return self.dbpool

    #创建数据库
    def insert(self, item):

        sql = ''
        if item['table_name'] == 'suggest':
            sql = "insert into suggest(acttitle,hhao,market_price,image_urls,content,video_url) values(%s,%s,%s,%s,%s,%s)"
        elif item['table_name'] == 'xinpin':
            sql = "insert into xinpin(acttitle,hhao,market_price,image_urls,content) values(%s,%s,%s,%s,%s)"

        #调用插入的方法
        query = self.dbpool.runInteraction(self._conditional_insert, sql, item)
        #调用异常处理方法
        query.addErrback(self._handle_error)

        return item

    #写入数据库中
    def _conditional_insert(self, tx, sql, item):
        params = (item['acttitle'], item['hhao'], item['market_price'],
                  item['image_urls'], item['desc'])
        if item['table_name'] == 'suggest':
            params = (*params,item['video_url'])
        tx.execute(sql, params)

    #错误处理方法

    def _handle_error(self, failue):
        print('--------------database operation exception!!-----------------')
        print(failue)