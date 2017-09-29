#encoding=utf8
from core.rock_clustering import rock_type
import heapq
import random
class my_heap:
    def __init__(self,initial=None,key = lambda x:x): ## 可以通过key来实现比较函数吗？？？
        # self.k = 20 # the size of this heap , i think it is useless in our problem
        self.key = key
        self._data = []

    def heapsize(self):
        return len(self._data)

    def push(self,item):
        '''
        自定义 push
        :param elem:
        :return:
        '''
        ## old
        # if len(self.data) < self.k:
        #     heapq.heappush(self.data.elem)
        # else:
        heapq.heappush(self._data,(self.key(item),item)) ##
        ## --->> 关键特性
        ## 这么做能成功的原因是不是因为： tuple 默认是比较第零个元素 呢？？，就相当于是key，
        ## 这样就可以实现自定义的比较函数了吧，方法，
        ##　将比较函数值放在tuple的第一个元素，比较对象在tuple 的第二个对象， 原来如此啊

    def pop(self):
        '''
        pop define by myself
        :return:
        '''
        if(len(self._data) > 1):
            return heapq.heappop(self._data)[1]
        else:
            return None

    def peek_top(self):
        '''
        peek max in the heap
        :return:
        '''
        if(len(self._data) > 1):
            return self._data[0][1]
        else:
            return None

    def delete(self,index):
        '''
        以对象id为目标在堆中删除对象，我的方法是以id找到该对象的索引，将堆中最后一个元素放到该位置，
        再进行堆的调整
        实验证明这么做是对的
        复杂度为Ｏ(logn)
        :return:
        '''
        if len(self._data)-1 == index:
            self._data.pop()
            return True
        self._data[index] = self._data[-1]
        self._data.pop()
        # print 'heap size is ',len(self._data), ' index ',index
        heapq._siftup(self._data,index) ##　TODO
        heapq._siftdown(self._data,0,index) ## TODO 可能会有问题　————没有问题
        return True

    def delete_by_attr(self,val,attr):
        '''
        如果存在返回True，否则返回False,
        :param val:
        :param attr:
        :return:
        '''
        idx = self.find_index_by_attr(val,attr)
        if idx == -1:
            return False
        return self.delete(idx)

    def find_index_by_attr(self,val,attr):
        '''
        如果存在返回该对象在堆中的索引，否则返回-1,
        :param val:
        :param attr:
        :return:
        '''
        hpsize = self.heapsize()
        if hpsize == 0:
            return -1
        for i in range(hpsize):
            v = getattr(self._data[i][1],attr)
            if val == v:
                return i
        return -1


    def display(self,i,j):
        '''
        显示堆中元素，ｉ起始位置，ｊ终止位置
        :param i:
        :param j:
        :return:
        '''
        for pos in range(i,j):
            print self._data[pos]

## test
def main():
    testlist = []
    num = 100
    myhp = my_heap(key = lambda item: -item.gkey)
    for i in range(100):
        # id = random.randint(0,100)
        id = i
        # gkey = random.randint(0,100)
        gkey = i + 5
        myhp.push(rock_type.rock_type(id, gkey))
    myhp.display(0,40)
    print 'len',len(myhp._data)
    for i in range(20):
        j = myhp.pop()
        if(j != None):
            print str(j.gkey) + '\t' + str(j.id)
    myhp.display(0,40)
    print 'len', len(myhp._data)
    myhp.delete(1)
    myhp.delete(2)
    myhp.delete(3)
    print 'seperate !!'
    myhp.display(0,40)
    print 'len', len(myhp._data)



if __name__ == '__main__':
    main()
    print 'ok!! '


