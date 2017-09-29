#encoding=utf-8
from core.rock_clustering import my_heap,rock_type
class rock_queue:
    '''
    堆的实现，包括global_heap 和local_heap,
    '''
    def __init__(self,rt_lens,id = -1,count=0): ## todo
        # 有默认值的参数要放在最后面
        '''
        构造函数
        :param ptree:核心数据结构，是一个平衡二叉堆
        :param rt:  用来标记以值为id的rock_type对象是否在堆中
        :param id:  TODO
        :param count: TODO
        '''
        self.rkheap = my_heap.my_heap(key=lambda x: -x.gkey)
        self.rt = [-1 for i in range(rt_lens)]
        self.id = id
        self.count = count

    def capacity(self):
        return len(self.rt)

    def size(self):
        return self.count

    def delete(self,id):
        '''
        根据rock_type的id对堆中相应元素进行删除
        :param id:
        :return:
        '''
        if self.rt[id] == None or self.rt[id] == -1:
            return False ## 堆中没有该对象
        flag = self.rkheap.delete_by_attr(id,'id')
        if flag:
            self.count = self.count -1
            self.rt[id] = -1
        return flag

    def insert(self,rkty):
        '''

        :param rkty:
        :return:
        '''
        if self.rt[rkty.id] != None and self.rt[rkty.id] != -1:
            return False
        self.rkheap.push(rkty)
        self.count += 1
        self.rt[rkty.id] = 1
        return True

    def insert_by_id(self,id,gkey):
        rkty = rock_type.rock_type(id,gkey)
        return self.insert(rkty)



    def update(self,id,gkey):
        '''

        :param id:
        :param gkey:
        :return:
        '''
        if self.rt[id] == None or self.rt[id] == -1:
            self.insert_by_id(id,gkey)
            self.count += 1
            return True
        ## 改进方案中直接使用rt[id]中存放有在对中的index,
        ## 现在没有采用改进的方案
        flag = self.rkheap.delete_by_attr(id,'id')
        if flag :
            self.rt[id] = -1
            self.count -= 1
            return self.insert_by_id(id,gkey)
        return False

    def get_max(self):
        if self.count == 0:
            return None
        return self.rkheap.peek_top()

    def extract_max(self):
        if self.count == 0:
            return None
        the_max = self.rkheap.pop()
        self.count -= 1
        self.rt[the_max.id] = -1
        return the_max.id