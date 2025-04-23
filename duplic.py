nums = [3, 1, 12, 7, 1, 3, 8, 8, 4]
def find_duplicates(nums):
    seen = set()
    duplicates = set()

    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return list(duplicates)

duplicate_elements = find_duplicates(nums)
print(f"Повторяющиеся элементы: {duplicate_elements}")
