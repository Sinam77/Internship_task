##1
from solutions import word_frequency
sentence = "python is easy and python is powerful"
print(word_frequency(sentence))
print(word_frequency("hello hello world"))

##2
from solutions import char_frequency
print(char_frequency("banana"))
print(char_frequency("hello"))

#3
from solutions import non_rep_char
print(non_rep_char("swiss"))
print(non_rep_char("aabb"))

#4
from solutions import anagrams
print(anagrams("listen", "silent"))
print(anagrams("hello", "world"))

# Q5
from solutions import first_repeat
print(first_repeat("programming"))
print(first_repeat("abcdef"))

# Q6
from solutions import move_zeros
print(move_zeros([0, 3, 0, 1, 2, 0, 4]))
print(move_zeros([1, 0, 2, 0, 3]))

# Q7
from solutions import second_highest
print(second_highest([10, 20, 40, 30, 40, 20]))
print(second_highest([5, 5, 5]))

# Q8
from solutions import remove_duplicates
print(remove_duplicates([4, 2, 4, 5, 2, 7, 5]))
print(remove_duplicates([1, 1, 2, 3, 3, 4]))

# Q9 
from solutions import missing_number
print(missing_number([1, 2, 4, 5, 6], 6))
print(missing_number([1, 3, 4, 5], 5))

# Q10
from solutions import find_pair
print(find_pair([2, 7, 11, 15], 9))
print(find_pair([1, 4, 6, 8], 10))

# Q11
from solutions import closest_to_zero
print(closest_to_zero([-8, -3, 2, 5, -2]))
print(closest_to_zero([-5, -1, 1, 4]))

# Q12
from solutions import common_elements
print(common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
print(common_elements([1, 2, 2, 3], [2, 3, 4]))

# Q13
from solutions import rotate_right
print(rotate_right([1, 2, 3, 4, 5], 2))
print(rotate_right([10, 20, 30, 40], 1))


# Q14
from solutions import max_consecutive_sum
print(max_consecutive_sum([4, 7, 2, 9, 5]))
print(max_consecutive_sum([10, 20, 5, 8]))


# Q15
from solutions import all_pairs
print(all_pairs([2, 4, 3, 5, 7, 8, 1], 9))
print(all_pairs([1, 2, 3, 4, 5], 6))
