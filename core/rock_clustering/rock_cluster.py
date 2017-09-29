#encoding=utf-8
import numpy as np
from utils import config
from core.rock_clustering import LINK,my_heap,rock_func,rock_queue,rock_type

class rock_cluster:
    def __init__(self,link = None):
        self.link = link

    def rock_algorithm(self,k,S,lens):
        link = rock_func.rock_func.compute_linknum(S,lens,k)
        q = [None for  i in range(len(link.setN))]
        # q = []
        for s in range(lens):
            print '1: ',s
            q[s] = rock_func.rock_func.build_local_heap(link,s)
            # tmp = rock_func.rock_func.build_local_heap(link, s)
            # q.append(tmp)
            # print 'q[0] _data length is ',len(q[0].rkheap._data)
        Q = rock_func.rock_func.build_global_heap(link,q)
        while Q.size() > k:
            print '2: ', Q.size()
            u = rock_func.rock_func.extract_max(Q)
            if u == 319:
                print 'here! '
            # print '2: ', Q.size()
            v = rock_func.rock_func.max(q[u])
            flag = rock_func.rock_func.delete(Q,v)
            # print '2: ', Q.size()
            print flag
            if flag == False:
                print ' here !'
            w = rock_func.rock_func.merge(u,v,link)
            q[w] = rock_queue.rock_queue(lens + lens - k)
            xset = rock_func.rock_func.union_element(u,v,q)
            for x in xset:
                # if x == w: 看来没有这种情况发生
                #     continue  ## 如果此时q[x]中的 x == w, 没必要将w自己也插入到w的本地堆中
                link.linkNum[x,w] = link.linkNum[x,u] + link.linkNum[x,v]
                print Q.size(), 'u ',u, 'v ',v,' x ',x
                # if Q.size() == 2995 and u == 2910 and v == 2994 and x == 11:
                #     print 'here! '
                rock_func.rock_func.delete(q[x],u)
                rock_func.rock_func.delete(q[x],v)
                rock_func.rock_func.insert(q[x],w,rock_func.rock_func.gFunc(x,w,link))
                ## 如果此时q[x]中的 x == w, 没必要将w自己也插入到w的本地堆中
                if Q.rt[x] == 1 :
                    rock_func.rock_func.insert(q[w],x,rock_func.rock_func.gFunc(x,w,link))
                    rock_func.rock_func.update(Q,x,q[x])
            rock_func.rock_func.insert_max_qw(Q,w,q[w])
            rock_func.rock_func.deallocate(q[u])
            rock_func.rock_func.deallocate(q[v])
            print '2: ', Q.size()
        ## loop ends
        linkids = link.sets[:]
        for i in range(lens):
            mid = i
            while mid != linkids[mid]:
                mid = linkids[mid]
            linkids[i] = mid
        linkids3 = [-1 for i in range(lens)]
        for i in range(lens):
            linkids3[i] = linkids[i]
        linkidset = set(linkids3)
        print len(linkidset)
        retdic = {}
        for k in linkidset:
            retdic[k] = []
        for k in range(lens):
            retdic[linkids3[k]].append(k)
        for k in retdic:
            print retdic[k]



def main():
    sim_mat_path = config.get_home_dir()
    sim_matrix = np.load(sim_mat_path + 'core/rock_clustering/link_matrix.npy')
    lens = len(sim_matrix)
    rc = rock_cluster()
    k = 40  ## todo 原来的是70 个簇
    print 'lens :' ,lens
    dm_ids = rc.rock_algorithm(k,sim_matrix,lens)
    print dm_ids

if __name__ == '__main__':
    main()
