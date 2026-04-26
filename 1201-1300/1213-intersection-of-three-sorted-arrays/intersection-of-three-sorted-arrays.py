class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        res, i, j, k = [], 0, 0, 0
        while i < len(arr1) and j < len(arr2) and k < len(arr3):
            if arr1[i] == arr2[j] == arr3[k]:
                res.append(arr1[i])
                i, j, k = i + 1, j + 1, k + 1
                continue
            
            mx = max(arr1[i], arr2[j], arr3[k])

            if arr1[i] < mx: i += 1
            if arr2[j] < mx: j += 1
            if arr3[k] < mx: k += 1

        return res


    def arraysIntersection2(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        s2, s3 = set(arr2), set(arr3)
        return [n for n in arr1 if n in s2 and n in s3]