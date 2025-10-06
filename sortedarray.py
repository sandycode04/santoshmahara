def findMedianSortedArrays(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    m, n = len(nums1), len(nums2)
    low, high = 0, m
    half_len = (m + n + 1) // 2

    while low <= high:
        i = (low + high) // 2
        j = half_len - i
        if i < m and nums2[j-1] > nums1[i]:
            low = i + 1
        elif i > 0 and nums1[i-1] > nums2[j]:
            high = i - 1
        else:
            max_left = max(nums1[i-1] if i > 0 else float('-inf'),
                           nums2[j-1] if j > 0 else float('-inf'))
            if (m + n) % 2 == 1:
                return max_left
            min_right = min(nums1[i] if i < m else float('inf'),
                            nums2[j] if j < n else float('inf'))
            return (max_left + min_right) / 2
