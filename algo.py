from math import ceil
import numpy as np 

class Sort():
    def __init__(self) -> None:
        self.arr = None  # the array to be sorted 
        self.prevArr = None 
        self.mode = 0  # mode of sorting 
        self.step = 0  # which step is the current sorting in 
        self.groups = 2 
    
    def initArr(self,arr):
        # numpy arr 
        self.arr = arr 
        self.prevArr = arr.copy() 

    def reset(self):
        self.step = 0 

    def nextstep(self):
        self.prevArr = self.arr.copy() 

        if self.mode == "insert":
            self.insertSort()
        elif self.mode == "halfInsert":
            self.halfInsertSort()
        elif self.mode == "hill":
            if self.step == ceil(self.arr.shape[0] / self.groups):
                self.hillSort()
            else:
                self.hillMerge()

        elif self.mode == "bubble":
            self.bubbleSort()
        elif self.mode == "quick":
            self.quickSort(0,len(self.arr)-1)
        elif self.mode == "choose":
            self.chooseSort()
        
    def insertSort(self):
        pos = self.step 
        val = self.arr[pos]
        for i in range(pos-1,-1,-1):
            if self.arr[i] > val:
                self.arr[i+1] = self.arr[i] 
                self.arr[i] = val 
            else: 
                break
        self.step += 1 

    def halfInsertSort(self):
        pos = self.step 
        val = self.arr[pos] 
        l = 0 
        r = pos-1 
        while l <= r : 
            mid = (l + r) // 2 
            if val > self.arr[mid]:
                l = mid + 1  # 
            else:
                r = mid - 1  # 

        for i in range(pos-1,r,-1):
            self.arr[i+1] = self.arr[i] 
        self.arr[r+1] = val
        # print(l,r)  
        self.step += 1 

    def hillSort(self):
        for i in range(self.groups):
            pos = i + self.step * self.groups
            if pos > self.arr.shape[0]:
                continue
            val = self.arr[pos]
            for j in range(pos-self.groups,-1,-self.groups):
                if self.arr[j] > val:
                    self.arr[j+self.groups] = self.arr[j] 
                    self.arr[j] = val 
                else:
                    break
        self.step += 1
    
    def hillMerge(self):
        self.insertSort()

    def bubbleSort(self):
        for i in range(0,self.arr.shape[0]-1):
            if self.arr[i] > self.arr[i+1]:
                temp = self.arr[i] 
                self.arr[i] = self.arr[i+1] 
                self.arr[i+1] = temp
                
        self.step += 1 

    def quickSort(self,l,r):
        if l >= r: 
            return 
        val = self.arr[l]
        i = l 
        j = r 
        while i<j : 
            while i< j and self.arr[j] > val:
                j -= 1  
            if i < j : 
                self.arr[i] = self.arr[j] 
                i += 1 
            while i < j and self.arr[i] < val: 
                i+= 1
            if i <j : 
                self.arr[j] = self.arr[i] 
                j -= 1

        self.arr[i] = val 
        self.quickSort(l,i-1)
        self.quickSort(i+1,r)


    def chooseSort(self):
        pos = self.step
        minimum = self.arr[pos]
        min_i = pos 
        for i in range(pos,self.arr.shape[0]):
            if self.arr[i] < minimum:
                minimum = self.arr[i] 
                min_i = i 
        temp = self.arr[pos] 
        self.arr[pos] = self.arr[min_i]
        self.arr[min_i] = temp 
                
        self.step += 1 


if __name__ == "__main__":
    s = Sort()
    s.arr = np.random.randint(1,100,(20,))
    print(s.arr)
    for i in range(s.arr.shape[0]):
        s.bubbleSort()
        print(s.arr)
