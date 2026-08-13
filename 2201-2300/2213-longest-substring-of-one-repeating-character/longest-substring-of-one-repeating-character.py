class Solution:
    def longestRepeating(
        self, s: str, queryCharacters: str, queryIndices: List[int]
    ) -> List[int]:
        n = len(s)
        pre = [0] * (4 * n)
        suf = [0] * (4 * n)
        maxLen = [0] * (4 * n)
        leftChar = [""] * (4 * n)
        rightChar = [""] * (4 * n)

        def build(u: int, l: int, r: int) -> None:
            if l == r:
                pre[u] = 1
                suf[u] = 1
                maxLen[u] = 1
                leftChar[u] = s[l]
                rightChar[u] = s[l]
                return
            mid = (l + r) >> 1
            build(u << 1, l, mid)
            build(u << 1 | 1, mid + 1, r)
            pushUp(u, l, r)

        def pushUp(u: int, l: int, r: int) -> None:
            mid = (l + r) >> 1
            leftLen = mid - l + 1
            rightLen = r - mid
            left = u << 1
            right = u << 1 | 1
            leftChar[u] = leftChar[left]
            rightChar[u] = rightChar[right]
            pre[u] = pre[left]
            if pre[left] == leftLen and rightChar[left] == leftChar[right]:
                pre[u] = pre[left] + pre[right]
            suf[u] = suf[right]
            if suf[right] == rightLen and rightChar[left] == leftChar[right]:
                suf[u] = suf[right] + suf[left]
            maxLen[u] = max(maxLen[left], maxLen[right])
            if rightChar[left] == leftChar[right]:
                maxLen[u] = max(maxLen[u], suf[left] + pre[right])

        def update(u: int, l: int, r: int, pos: int, ch: str) -> None:
            if l == r:
                leftChar[u] = ch
                rightChar[u] = ch
                return
            mid = (l + r) >> 1
            if pos <= mid:
                update(u << 1, l, mid, pos, ch)
            else:
                update(u << 1 | 1, mid + 1, r, pos, ch)
            pushUp(u, l, r)

        build(1, 0, n - 1)
        k = len(queryIndices)
        ans = []
        for i in range(k):
            update(1, 0, n - 1, queryIndices[i], queryCharacters[i])
            ans.append(maxLen[1])
        return ans

    def longestRepeating2(
        self, s: str, queryCharacters: str, queryIndices: List[int]
    ) -> List[int]:
        n = len(s)
        s = list(s)
        segs = SortedList()
        lens = SortedList()

        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            segs.add((i, j - 1))
            lens.add(j - i)
            i = j

        k = len(queryIndices)
        ans = []

        for q in range(k):
            pos = queryIndices[q]
            ch = queryCharacters[q]

            if s[pos] != ch:
                idx = segs.bisect_right((pos, n)) - 1
                L, R = segs[idx]
                segs.pop(idx)
                lens.remove(R - L + 1)

                if L <= pos - 1:
                    segs.add((L, pos - 1))
                    lens.add(pos - L)
                if pos + 1 <= R:
                    segs.add((pos + 1, R))
                    lens.add(R - pos)

                newL, newR = pos, pos

                if pos + 1 < n and s[pos + 1] == ch:
                    idx2 = segs.bisect_left((pos + 1, -1))
                    if idx2 < len(segs) and segs[idx2][0] == pos + 1:
                        rightL, rightR = segs[idx2]
                        lens.remove(rightR - rightL + 1)
                        newR = rightR
                        segs.pop(idx2)

                if pos > 0 and s[pos - 1] == ch:
                    idx3 = segs.bisect_right((pos - 1, n)) - 1
                    if idx3 >= 0 and segs[idx3][1] == pos - 1:
                        leftL, leftR = segs[idx3]
                        lens.remove(leftR - leftL + 1)
                        newL = leftL
                        segs.pop(idx3)

                segs.add((newL, newR))
                lens.add(newR - newL + 1)
                s[pos] = ch

            ans.append(lens[-1])

        return ans