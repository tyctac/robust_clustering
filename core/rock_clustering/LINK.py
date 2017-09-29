#encoding=utf-8
import numpy as np
class LINK:
    def __init__(self,Length,k):
        ## self.linkNum may have problems
        self.lens = Length + Length -k ## k is the number of cluster
        self.linkNum = np.zeros((self.lens, self.lens))
        self.setN = []
        self.sets = []
        for i in range(self.lens):
            self.setN.append(1)
            self.sets.append(i)
        self.lens = Length
        self.now = self.lens

    def new_element(self):
        self.now += 1
        return self.now -1