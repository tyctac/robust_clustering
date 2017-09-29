#encoding=utf-8
import numpy as np
import threading
from database_oper import mongo_obj
from similarity import domain_sim
def get_dm_list():
    mo = mongo_obj.MongoOper()
    dm_obj = mo.db['dm_obj']
    dm_objs = dm_obj.find()
    dm_list = []
    for dm in dm_objs:
        dm_list.append(dm)
    # for x in dm_list:
    #     print x
    print len(dm_list)
    return dm_list

def calc_part(sim_matrix,link_matrix,dm_list,start,end):
    lens = len(sim_matrix)
    for i in range(start,end):
        print '>>',start,'<< ',i
        for j in range(lens):
            # print j
            sim = calculate_simularity(dm_list[i], dm_list[j])
            sim_matrix[i,j] = sim
            if sim > 0:
                link_matrix[i,j] = 1
    print '>>',start, ' ok !'

def get_the_matrix():
    dm_list = get_dm_list()
    # lens = len(dm_list)
    lens = 300 ## >>>>> TODO 原来是3000
    link_mat = np.zeros((lens, lens))
    sim_mat = np.zeros((lens, lens))
    threads = []
    t1 = threading.Thread(target=calc_part,args=(sim_mat,link_mat,dm_list,0,50))
    threads.append(t1)
    t2 = threading.Thread(target=calc_part, args=(sim_mat, link_mat, dm_list, 50, 100))
    threads.append(t2)
    t3 = threading.Thread(target=calc_part, args=(sim_mat, link_mat, dm_list, 100, 150))
    threads.append(t3)
    t4 = threading.Thread(target=calc_part, args=(sim_mat, link_mat, dm_list, 150, 200))
    threads.append(t4)
    t5 = threading.Thread(target=calc_part, args=(sim_mat, link_mat, dm_list, 200, 250))
    threads.append(t5)
    t6 = threading.Thread(target=calc_part, args=(sim_mat, link_mat, dm_list, 250, 300))
    threads.append(t6)
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()
    np.save('sim_matrix', sim_mat)
    np.save('link_matrix', link_mat)
    print 'done! '
    return (sim_mat, link_mat)



def get_sim_matrix(): ## obsolete
    dm_list = get_dm_list()
    sm = 0
    lens = len(dm_list)
    link_mat = np.zeros((lens,lens))
    sim_mat = np.zeros((lens,lens))
    i = 0
    for i in range(lens):
        print '**********************>>>>>>',i
        i += 1
        for j in range(lens):
            sm += 1
            sim = calculate_simularity(dm_list[i],dm_list[j])
            sim_mat[i,j] = sim
            if sim > 0:
                link_mat[i,j] = 1
    np.save('sim_matrix_small',sim_mat)
    np.save('link_matrix_small',link_mat)
    return (sim_mat,link_mat)

def test_threshold():
    dm_list = get_dm_list()
    sm = 0
    ret = []
    for i in range(50,100):
        for j in range(200,250):
            sm += 1
            sim = calculate_simularity(dm_list[i],dm_list[j])
            if sim > 0:
                ret.append((i,j,sim))
    for tp in ret:
        print tp
    print len(ret)

def calculate_simularity(dm1,dm2):
    return domain_sim.Domain_sim.get_similarity(dm1,dm2)


def main():
    # get_the_matrix()
    dm_lst = get_dm_list()
    lst_lens = len(dm_lst)
    while True:
        index = (int)(raw_input('input the index of domain object: '))
        print dm_lst[index]

if __name__ == '__main__':
    main()