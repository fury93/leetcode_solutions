import numpy as np
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        a = [i * n + j for i in range(n) for j in range(n) if img1[i][j]]
        b = [i * n + j for i in range(n) for j in range(n) if img2[i][j]]
        if not a or not b:
            return 0
        w = 2 * n
        counts = [0] * (w * w)
        best = 0
        for pa in a:
            ai, aj = divmod(pa, n)
            base = (n - ai) * w + (n - aj)
            for pb in b:
                bi, bj = divmod(pb, n)
                k = base + bi * w + bj
                v = counts[k] + 1
                counts[k] = v
                if v > best:
                    best = v
        return best
        
    def largestOverlap2(self, A: List[List[int]], B: List[List[int]]) -> int:
        A = np.array(A)
        B = np.array(B)

        dim = len(A)
        # extend the matrix to a wider range for the later kernel extraction.
        B_padded = np.pad(B, dim-1, mode='constant', constant_values=(0, 0))

        max_overlaps = 0
        for x_shift in range(dim*2 - 1):
            for y_shift in range(dim* 2 - 1):
                # extract a kernel from the padded matrix
                kernel = B_padded[x_shift:x_shift+dim, y_shift:y_shift+dim]
                # convolution between A and kernel
                non_zeros = np.sum(A * kernel)
                max_overlaps = max(max_overlaps, non_zeros)

        return max_overlaps