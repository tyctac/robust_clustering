#encoding=utf-8
import pymysql
from utils import config


class MysqldbHelper:
    def __init__(self):
        self.conn = object()

    def set_conn(self):
        # self.conn = pymysql.connect(host=h,port = pt,user = u,passwd =p,db = dbname)
        self.conn = pymysql.connect(host='192.168.4.134', port=3306, user='lzw', passwd='tca.iscas', db='domain_db',charset='utf8')

    def get_url(self):
        self.set_conn()
        cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        ## 或者这样写： cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        cur.execute("select Domain_Name,Registrant_Name,Creation_Date from Domain_WhoisInfo limit 100")
        for r in cur.fetchall():
            print(r)
        self.conn.close()

    def get_domains(self,date_threshold): ## DONE
        '''
        选择创建时间大于某一天的所有域名
        :param date_threshold:
        :return:
        '''
        self.set_conn()
        cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        cur.execute("select DISTINCT(Domain_Name) from Domain_WhoisInfo where Creation_Date > '" + date_threshold + "'")
        lst = []
        for r in cur.fetchall():
            # print r
            lst.append(r['Domain_Name'])
        self.conn.close()
        return lst

    def get_domain_info(self,domain_name):
        self.set_conn()
        cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        cur.execute('select * from Domain_WhoisInfo WHERE Domain_Name = "' + domain_name + '"')
        ret = []
        for r in cur.fetchall():
            ret.append(r)
        return ret

    def get_Admin_Email(self):
        self.set_conn()
        cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        cur.execute('select Domain_Name,Admin_Email from Domain_WhoisInfo WHERE Creation_Date > "2017-01-01"')
        ret = []
        for r in cur.fetchall():
            if r not in ret:
                ret.append(r)
        return ret

def main1():
    db = MysqldbHelper()
    ret = db.get_Admin_Email()
    print ret

def main0():
    db = MysqldbHelper()
    # ret = db.get_url()
    time_limit = config.get_time_limit()
    ret = db.get_domains(time_limit)
    print ret

def main():
    db = MysqldbHelper()
    time_limit = config.get_time_limit()
    ret = db.get_domain_info('c87577.com')
    print ret

if __name__ == "__main__":
    main1()


# Domain_Name
# Domain_IP
# Domain_ID
# Whois_Server
# Registrar_URL
# Creation_Date
# Expiration_Date
# Updated_Date
# Registrar_Name
# Registrar_ID
# Registrar_Phone
# Registrar_Email
# Domain_State
# Registrant_ID
# Registrant_Name
# Registrant_Org
# Registrant_Street
# Registrant_City
# Registrant_State
# Registrant_Zipcode
# Registrant_Country
# Registrant_Phone
# Registrant_Phone2
# Registrant_Fax
# Registrant_Fax2
# Registrant_Email
# Admin_ID
# Admin_Name
# Admin_Org
# Admin_Street
# Admin_City
# Admin_State
# Admin_Zipcode
# Admin_Country
# Admin_Phone
# Admin_Phone2
# Admin_Fax
# Admin_Fax2
# Admin_Email
# Billing_ID
# Billing_Name
# Billing_Org
# Billing_Street
# Billing_City
# Billing_State
# Billing_Zipcode
# Billing_Country
# Billing_Phone
# Billing_Phone2
# Billing_Fax
# Billing_Fax2
# Billing_Email
# Tech_ID
# Tech_Name
# Tech_Org
# Tech_Street
# Tech_City
# Tech_State
# Tech_Zipcode
# Tech_Country
# Tech_Phone
# Tech_Phone2
# Tech_Fax
# Tech_Fax2
# Tech_Email
# DnsServer
# WhoisData_Time
# Domain_Url
# iskey
