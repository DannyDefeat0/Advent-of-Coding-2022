#key info, both lists are pre-sorted.
def merge(nums1, m, nums2, n):
    output = nums1
    k = m + n
    j = 0
    while j < m+1:
        for i in range(n-1):
            print(nums2[i])
            if nums2[i] < nums1[j]:
                output[i] = nums2[i]
                output[i+1] = nums1[j]
                j += 1
            elif nums2[i] >= nums1[j]:
                while nums2[i] > nums1[j]:
                    j += 1
                output.insert(j+1,nums2[i])
                output.pop()
            return output
def test_merge():
    assert merge([1,2,3,0,0,0],3,[2,5,6],3) == [1,2,2,3,5,6]
    #starting with 2, we can see it's greater than 1 and but less than 3 and that 5,6 go at the end
    #step 1
    #output = [1,2,2,3,0,0]
    #we checked indexes 0,1,2
    #step 2
    #output = [1,2,2,3,5,0]
    #we checked index 4
    #step 3
    #output = [1,2,2,3,5,6]
    #we checked index 5
print(merge([1,2,3,0,0,0],3,[2,5,6],3))

test_merge()
