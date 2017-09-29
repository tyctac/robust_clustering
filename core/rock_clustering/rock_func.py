#encoding=utf-8
from core.rock_clustering import rock_queue,rock_type,LINK
import math
class rock_func:
    @staticmethod
    def compute_linknum(u,lens,k):
        '''
        根据邻居矩阵u计算共同连接数对象LINK
        :param u: 邻居矩阵 , numpy 矩阵(len*len)
        :param len:
        :param k:
        :return:
        '''
        link = LINK.LINK(lens,k)
        # inlist = []
        # top = [0 for i in range(len)]
        # for i in range(len):
        #     for j in range(len):
        #         if u[i,j]:
        #             inlist[i,top[i]] = j
        #             top[i] += 1
        # for i in range(len):
        #     sumn = top[i]
        #     for j in range(sumn):
        #         pass ## TODO using matrix
        link_N = u*u
        for i in range(lens):
            for j in range(lens):
                link.linkNum[i,j] = link_N[i,j]
        return link

    @staticmethod
    def gFunc(i,j,link):
        '''
        calculate measure function
        :param i: cluster i
        :param j: cluster j
        :param link:  link object
        :return: double value
        '''
        w = 0.5
        mi = 1.0 + 2.0*w
        return (link.linkNum[i,j]) / ( math.pow((link.setN[i] + link.setN[j]), mi) - math.pow(link.setN[i],mi) - math.pow(link.setN[j],mi))

    @staticmethod
    def build_local_heap(link,s):
        '''

        :param link:
        :param s:
        :return:
        '''
        qs = rock_queue.rock_queue(len(link.setN)) ## len(link.setN) 表示共有多少个簇
        for i in range(link.lens):
            if(i == s) :
                continue
            gkey = rock_func.gFunc(i,s,link)
            qs.insert_by_id(i,gkey)
        return qs

    @staticmethod
    def build_global_heap(link,q):
        '''
        q 是本地堆数组
        :param link:
        :param q:
        :return:
        '''
        gheap = rock_queue.rock_queue(len(link.setN))
        for i in range(link.lens):
            iMax = q[i].get_max()
            if iMax != None:
                irt = rock_type.rock_type(i,iMax.gkey)
                gheap.insert(irt)
        return gheap

    @staticmethod
    def size(self,Q):
        return Q.size()

    @staticmethod
    def extract_max(Q):
        return Q.extract_max()

    @staticmethod
    def max(qu):
        return qu.get_max().id

    @staticmethod
    def delete(queue,id):
        if queue == None:
            return False
        return queue.delete(id)

    @staticmethod
    def merge(u,v,link):
        w = link.new_element()
        print w,' ',u,' ','v' ,v,' here accident occur!!! '
        print len(link.setN)
        link.setN[w] = link.setN[u] + link.setN[v] ## 暂时看来setN[i]表示簇i中有多少初始簇(个体)
        link.sets[v] = w
        link.sets[u] = w
        return w

    @staticmethod
    def union_element(u,v,q):
        '''
        返回u,v的共同邻居
        :param u: cluster u
        :param v: cluster v
        :param q: local_heap array
        :return:
        '''
        lens = q[u].capacity() ## 所有的capacity 都一样大??
        lst = []
        for i in range(lens):
            if q[u].rt[i] == 1 or q[v].rt[i] == 1:
                lst.append(i)
        return lst

    @staticmethod
    def deallocate(queue):
        queue = None

    @staticmethod
    def insert(queue,w,key):
        queue.insert_by_id(w,key)
        return True

    @staticmethod
    def insert_max_qw(Q,w,qw):
        return Q.insert_by_id(w,qw.get_max().gkey)

    @staticmethod
    def update(Q,x,qx):
        if qx == None:
            return
        Q.update(x,qx.get_max().gkey)
