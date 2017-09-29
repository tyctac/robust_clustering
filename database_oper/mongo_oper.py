#encoding=utf-8
from database_oper import mysql_obj
from database_oper import mongo_obj
from utils import config
from datetime import datetime

def store_domain(collection_name): ## at this circumustance ,collection_name should always be 'domain'
    '''
    只能执行一遍,没有去除重复
    :param collection_name:
    :return:
    '''
    mo = mongo_obj.MongoOper()
    domn = mo.db[collection_name]
    sqlhlp = mysql_obj.MysqldbHelper()
    domlist = sqlhlp.get_domains(config.get_time_limit())
    domain_ob = {}
    domain_ob['domains'] = domlist
    domn.insert(domain_ob)


def get_admin_email_dic():
    domains = get_domain_names('domain')
    ret_dic = {}
    sqlhlp = mysql_obj.MysqldbHelper()
    i = 0
    admin_email_obj = sqlhlp.get_Admin_Email()
    for ob in admin_email_obj:
        print i
        i += 1
        # if ob['Domain_Name'] == None or ob['Domain_Name'].strip() == '':
        #     print 'error!!'
        domain_name = ob['Domain_Name'].strip()
        admin_email = ob['Admin_Email'].strip()
        if domain_name not in ret_dic:
            ret_dic[domain_name] = []
            ret_dic[domain_name].append(admin_email)
        else:
            if admin_email not in ret_dic[domain_name]:
                ret_dic[domain_name].append(admin_email)
    return ret_dic

def recorrect():  ## 粗心大意的结果,多花费了一个小时时间来擦屁股.....
    print 'this is recorrect!!!'
    mo = mongo_obj.MongoOper()
    domn = mo.db['domain_obj']
    ret_dic = get_admin_email_dic()
    dm_obj = mo.db['dm_obj']
    domain_objs = domn.find()
    i = 0
    for cu in domain_objs:
        print i
        i += 1
        tmp = {}
        tmp['name'] = cu['name']
        tmp['ip'] = cu['ip']
        tmp['person'] = list(set(cu['person']))
        tmp['phone'] = list(set(cu['phone']))
        xxx = ret_dic[cu['name']]
        tmp['email'] = list(set(xxx))
        dm_obj.insert(tmp)



def get_domain_names(collection_name):
    mo = mongo_obj.MongoOper()
    domn = mo.db[collection_name]
    cur = domn.find_one({})
    return cur['domains']
    # for cu in cur:
    #     print cu

def store_dm_obj(domain_names,collection_name): ## collection_name should be 'domain_obj'
    mo = mongo_obj.MongoOper()
    domn = mo.db[collection_name]
    sqlhlp = mysql_obj.MysqldbHelper()
    lens = len(domain_names)
    i = 1
    for dm in domain_names:
        print i
        i += 1
        obj_list = sqlhlp.get_domain_info(dm)
        tmp = {}
        tmp['name'] = dm
        tmp['person'] = []
        tmp['phone'] = []
        tmp['email'] = []
        tmp['ip'] = ''
        for ob in obj_list:
            if ob['Domain_IP'].strip() != '' and ob['Domain_IP'] != None:
                tmp['ip'] = ob['Domain_IP']
            if ob['Registrar_Name'].strip() != '' and ob['Registrar_Name'] != None:
                tmp['person'].append(ob['Registrar_Name'])
            if ob['Admin_Name'].strip() != '' and ob['Admin_Name'] != None:
                tmp['person'].append(ob['Admin_Name'])
            if ob['Tech_Name'].strip() != '' and ob['Tech_Name'] != None:
                tmp['person'].append(ob['Tech_Name'])
            if ob['Domain_IP'].strip() != '' and ob['Domain_IP'] != None:
                tmp['ip'] = ob['Domain_IP']
            ## phone
            if ob['Registrar_Phone'].strip() != '' and ob['Registrar_Phone'] != None:
                tmp['phone'].append(ob['Registrar_Phone'])
            if ob['Admin_Phone'].strip() != '' and ob['Admin_Phone'] != None:
                tmp['phone'].append(ob['Admin_Phone'])
            if ob['Tech_Phone'].strip() != '' and ob['Tech_Phone'] != None:
                tmp['phone'].append(ob['Tech_Phone'])
            ## email
            if ob['Registrar_Email'].strip() != '' and ob['Registrar_Email'] != None:
                tmp['email'].append(ob['Registrar_Email'])
            if ob['Admin_Email'].strip() != '' and ob['Admin_Email'] != None:
                tmp['email'].append(ob['Admin_Phone'])
            if ob['Tech_Email'].strip() != '' and ob['Tech_Email'] != None:
                tmp['email'].append(ob['Tech_Email'])
        domn.insert(tmp)

def store_all_domain_obj(collection_name): ## at this circumustance, collection_name shall be: 'domain_obj'
    pass

def main():
    # domain_lst = get_domain_names('domain')
    # store_dm_obj(domain_lst, 'domain_obj')
    # print 'ok'
    recorrect()

if __name__ == '__main__':
    main()

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
