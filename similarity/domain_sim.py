#encoding=utf-8
from utils import levenshtein_distance,config
class Domain_sim():
    weight = [1,10,10,10]
    def __init__(self,weight = [1,1,1,1]):  ## 定义一些配置信息
        self.weight = weight ## name_similarity,person,phone,email

    @staticmethod
    def set_weight(wt):
        Domain_sim.weight = wt

    @staticmethod
    def name_similarity(name1,name2):
        return levenshtein_distance.get_ld(name1,name2) ## u'LCCXZS.COM''  u'LCCXZS.COM'

    @staticmethod
    def reg_person_similarity(p1,p2):
        '''
        注册人信息的相似度，如何计算
        :return:
        '''
        if  p1 == p2:
            return 1 * config.get_reg_person_weight()

    @staticmethod
    def phone_similarity(phone1,phone2):
        pass

    @staticmethod
    def jaccard_coeffient(lst1,lst2): ## 如果都为空??
        len1 = len(lst1)
        len2 = len(lst2)
        if len1 == 0 or len2 == 0:
            return 0
        cnt = 0
        for ele in lst1:
            if ele in lst2:
               cnt += 1
        return cnt/float(len1 + len2)

    @staticmethod
    def get_similarity(obj1,obj2): ## 计算两个域名实体的相似度
        # print '  '
        # print obj1,'   ',obj2
        name1 = str(obj1['name']).lower()
        name2 = str(obj2['name']).lower()
        if name1[:4] == 'www.':
            name1 = name1[4:]
        if name2[:4] == 'www.':
            name2 = name1[4:]
        name_sim = Domain_sim.name_similarity(name1,name2)
        if name_sim > 4:
            name_sim = 0
        else:
            name_sim = 16 - name_sim*name_sim
        # print 'name_sim of ', obj1['name'],' and ',obj2['name'] , ' is ',name_sim
        person_sim = Domain_sim.jaccard_coeffient(obj1['person'],obj2['person'])
        # print 'person_sim ',person_sim
        phone_sim = Domain_sim.jaccard_coeffient(obj1['phone'],obj2['phone'])
        # print 'phone_sim ',phone_sim
        email_sim = Domain_sim.jaccard_coeffient(obj1['email'],obj2['email'])
        # print 'email_sim ',email_sim
        sim = 0
        sim += name_sim * Domain_sim.weight[0]
        sim += person_sim * Domain_sim.weight[1]
        sim += phone_sim * Domain_sim.weight[2]
        sim += email_sim * Domain_sim.weight[3]
        # print 'sim ',sim
        # print '<<++++++++++++++++++'
        return sim

    def reg_date_similarity(self):
        '''
        时间相似性指标：
        这里使用两者之间的间距，
        使用两年的时间归一化
                先弄清楚格式再写代码
        :return:
        '''
        pass

def main():
    name1 = str(u'iphone-icloudr.com')
    name2 = str(u'wepci.com')
    dis = levenshtein_distance.get_ld(name1,name2)
    print dis

if __name__ == '__main__':
    main()
