def split_and_sort(nums):
    # check if input list length is less than or equal to 20
    if len(nums) > 20:
        return "Error: Input list should not contain more than 20 integers."

    # check if 0 is in the input list
    if 0 in nums:
        return "Error: The number 0 is not a valid input."
    
    # Convert list of integers into set --> Remove duplicate values
    nums = set(nums)

    # filter odd and even numbers into two separate lists
    odd_nums = [num for num in nums if num % 2 == 1]
    even_nums = [num for num in nums if num % 2 == 0]

    # remove duplicates and sort
    odd_nums = sorted(odd_nums)
    even_nums = sorted(even_nums)

    return odd_nums, even_nums

print("### Test Case 1 ###")
odd_nums, even_nums = split_and_sort([2, 12, 24, 26, 28, 32])
print(f"Even Numbers: {even_nums} --- Expected: {[2, 12, 24, 26, 28, 32]}")
print(f"Odd Numbers: {odd_nums} --- Expected: {[2, 12, 24, 26, 28, 32]}\n")

print("### Test Case 2 ###")
odd_nums, even_nums = split_and_sort([11, 12, 13, 14, 15, 16, 17,18, 19, 20])
print(f"Even Numbers: {even_nums} --- Expected: {[12, 14, 16, 18, 20]}")
print(f"Odd Numbers: {odd_nums} --- Expected: {[11, 13, 15, 17, 19]}\n")

print("### Test Case 3 ###")
odd_nums, even_nums = split_and_sort([100, 87, 56, 55, 41, 36, 31, 30, 25, 22, 15, 10, 5, 2])
print(f"Even Numbers: {even_nums} --- Expected: {[2, 10, 22, 30, 36, 56, 100]}")
print(f"Odd Numbers: {odd_nums} --- Expected: {[5, 15, 25, 31, 41, 55, 87]}\n")

print("### Test Case 4 ###")
odd_nums, even_nums = split_and_sort([100, 50, 62, 102, 4])
print(f"Even Numbers: {even_nums} --- Expected: {[4, 50, 62, 100, 102]}")
print(f"Odd Numbers: {odd_nums} --- Expected: {[]}\n")

print("### Test Case 5 ###")
odd_nums, even_nums = split_and_sort([3, 7, 5, 13, 9])
print(f"Even Numbers: {even_nums} --- Expected: {[]}")
print(f"Odd Numbers: {odd_nums} --- Expected: {[3, 5, 7, 9, 13]}\n")

print("### Test Case 6 ###")
odd_nums, even_nums = split_and_sort([1, 13, 16, 42, 13, 20, 3, 16, 21, 1, 29, 13, 8, 11, 1])
print(f"Even Numbers: {even_nums} --- Expected: {[8, 16, 20, 42]}")
print(f"Odd Numbers: {odd_nums} --- Expected: {[1, 3, 11, 13, 21, 29]}\n")