class Data:
    def__init___(self):
        self.nums = [1,2,3,4,5]
    def change_data(self,index,n):
        self.nums[index] = n

data_one = Data()
data_one.nums[0] = 100
print(data_one.nums)

data_two = Data()
data_two.change_data(0,100)
print(data_two.nums)