class domain():
    def __init__(self,name = None,regist_person = None,regist_date = None):
        self.name = name
        self.reg_person = regist_person
        self.reg_date = regist_date
    ##需要将域名信息存入mongodb

    def initial(self):
        pass