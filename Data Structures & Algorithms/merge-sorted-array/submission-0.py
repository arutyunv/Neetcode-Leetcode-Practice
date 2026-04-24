### Three Pointers with Extra Space ###

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Define the index of the last position to fill in nums1.
        last = m + n - 1

        # Pointers to the last valid elements in the two arrays.
        i, j = m - 1, n - 1

        # While both piles have elements, place the larger at the end.
        while i >= 0 and j >= 0:
            # If nums1[i] is larger, move it to the end.
            if nums1[i] > nums2[j]:
                nums1[last] = nums1[i]
                i -= 1
            # Otherwise, move nums2[j] to the end.
            else:
                nums1[last] = nums2[j]
                j -= 1
            # Move the last-fill position backward.
            last -= 1

        # 5. If there are remaining elements in nums2, copy them over.
        while j >= 0:
            nums1[last] = nums2[j]
            j -= 1
            last -= 1


        
        