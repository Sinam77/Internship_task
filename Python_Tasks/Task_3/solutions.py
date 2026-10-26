# Q1

def word_frequency(sentence):
    words = sentence.split()
    freq = {}

    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    return freq

# Q2

def char_frequency(word):
    freq={}

    for i in word:
        if i in freq:
            freq[i] +=1
        else:
            freq[i] =1

    return freq


# Q3

def non_rep_char(word):
    freq = {}

    for i in word:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    for i in word:
        if freq[i] == 1:
            return i

    return None


#Q4
def anagrams(s1,s2):
    freq1={}
    freq2={}

    for i in s1:
        if i in freq1:
            freq1[i] += 1
        else:
            freq1[i] = 1

    for i in s2:
        if i in freq2:
            freq2[i] += 1
        else:
            freq2[i] = 1
    return freq1==freq2
    
#5

def first_repeat(word):
    seen =[]

    for i in word :
        if i in seen:
            return i
        else:
            seen.append(i)

    return None

#6

def move_zeros(num):
    non_zero = []
    zeros = []

    for i in num:
        if i == 0:
            zeros.append(i)
        else:
            non_zero.append(i)

    return non_zero + zeros

#7

def second_highest(nums):
    unique = set(nums)

    if len(unique) < 2:
        return None

    sorted_nums = sorted(unique, reverse=True)

    return sorted_nums[1]

# Q8

def remove_duplicates(nums):
    result = []

    for i in nums:
        if i not in result:
            result.append(i)

    return result

# Q9

def missing_number(nums, N):
    total = N * (N + 1) // 2
    actual = sum(nums)

    return total - actual

# Q10

def find_pair(nums, target):

    for j in range(1, len(nums)):
        for i in range(j):
            if nums[i] + nums[j] == target:
                return [nums[i], nums[j]]

    return []

# Q11
def closest_to_zero(nums):
    closest = nums[0]

    for i in nums:
        if abs(i) < abs(closest):
            closest = i

        elif abs(i) == abs(closest) and i > closest:
            closest = i

    return closest

# Q12

def common_elements(list1, list2):
    result = []

    for i in list1:
        if i in list2 and i not in result:
            result.append(i)

    return result

# Q13

def rotate_right(nums, k):
    if len(nums) == 0:
        return []

    k = k % len(nums)

    return nums[-k:] + nums[:-k] if k != 0 else nums[:]

# Q14

def max_consecutive_sum(nums):
    max_sum = nums[0] + nums[1]

    for i in range(len(nums) - 1):
        current_sum = nums[i] + nums[i + 1]

        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum

# Q15
def all_pairs(nums, target):
    result = []

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):

            if nums[i] + nums[j] == target:
                pair = sorted([nums[i], nums[j]])

                if pair not in result:
                    result.append(pair)

    result.sort()

    return result