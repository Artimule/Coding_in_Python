'''Input: a[] = {1, 3, 4, 2, 6, 5, 8, 7}
Output: Mean = 4.5, Median = 4.5
Explanation: Sum of the elements is 1 + 3 + 4 + 2 + 6 + 5 + 8 + 7 = 36, Mean = 36/8 = 4.5
Since number of elements are even, median is average of 4th and 5th largest elements, which means Median = (4 + 5)/2 = 4.5

Input: a[] = {4, 4, 4, 4, 4}
Output: Mean = 4, Median = 4 

To find median:
First, simply sort the array
Then, check if the number of elements present in the array is even or odd
If odd, then simply return the mid value of the array
Else, the median is the average of the two middle values

To find Mean:
At first, find the sum of all the numbers present in the array.
Then, simply divide the resulted sum by the size of the array

'''


def findMean(a, n):
 
    sum = 0
    for i in range(0, n):
        sum += a[i]
 
    return float(sum/n)
 
# Function for calculating median
 
 
def findMedian(a, n):
 
    # First we sort the array
    sorted(a)
 
    # check for even case
    if n % 2 != 0:
        return float(a[int(n/2)])
 
    return float((a[int((n-1)/2)] +
                  a[int(n/2)])/2.0)
 
 
# Driver code
a = [1, 3, 4, 2, 7, 5, 8, 6]
n = len(a)

# Function call
print("Mean =", findMean(a, n))
print("Median =", findMedian(a, n))
