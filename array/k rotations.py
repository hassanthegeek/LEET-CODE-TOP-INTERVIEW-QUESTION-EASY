from typing import List

class Making:
    def rotate(self, nums: List[int], k: int) -> None:
        size = len(nums)
        if k > size:
            k = k % size
        self.reverse(nums,size-k,size-1)
        self.reverse(nums,0,size-k-1) 
        self.reverse(nums,0,size-1)
        return nums


    def reverse(self,arr,start_index,end_index):
        size = end_index - start_index + 1
        for i in range(0,size):
            if i < size // 2:
                temp = arr[start_index]
                arr[start_index] = arr[end_index]
                arr[end_index] = temp
                end_index -= 1
                start_index += 1
            else:
                break




# while True:
m = Making()
# l = input().split(',')
# l = [int(a) for a in l]
# s = int(input())
l = [1,2,3,4,5,6]
m.rotate(l,11)
print(l)
# l = [1,2,3,4,5,6,7]
# m.rotate(l,2)
# print(l)
# print(m.rotate(l,s))