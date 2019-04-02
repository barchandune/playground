'''
FindMiddleIndex
	 int[] num = { 2, 4, 4, 5, 4, 1 }
'''

class Solution():

    def find_middle_index_with_bance_sum(self, nums):

        left_sum = nums[0]
        right_sum = nums[len(nums)-1]

        i = 0
        j = len(nums) - 1

        while(True):

            if i + 1 == j:
                if left_sum == right_sum:
                    return j
                else:
                    return "Left and Right side not balanced"
            else:
                #print("i {} j {}".format(i,j))
                if left_sum == right_sum:
                    i += 1
                    j -= 1
                    left_sum = left_sum + nums[i]
                    right_sum = right_sum + nums[j]

                elif left_sum > right_sum:
                    j -=1
                    if j>0:
                        right_sum = right_sum + nums[j]

                elif left_sum < right_sum:
                    i +=1
                    if i <len(nums)-1:
                        left_sum = left_sum + nums[i]

sol = Solution()
print(sol.find_middle_index_with_bance_sum(nums = [200, 4, 4, 2, 5, 6, 20]))