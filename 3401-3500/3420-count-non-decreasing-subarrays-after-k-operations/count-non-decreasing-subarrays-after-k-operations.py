class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        cost = 0
        queue = Deque([(nums[-1], 1)])
        res = 1
        back = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            cur = nums[i]
            cnt = 1

            while queue and queue[-1][0] < cur:
                lesser, count = queue.pop()
                cnt += count
                cost += (cur-lesser) * count
            queue.append((cur, cnt))
            while cost > k:
                more, count = queue.popleft()
                count -= 1
                cost -= (more-nums[back])
                back -= 1
                if count > 0:
                    queue.appendleft((more, count))

            res += back - i + 1
        return res

    def countNonDecreasingSubarrays2(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0
        operations = 0
        # Maintain the window maximum with a priority queue
        q = []
        # Record the set of elements covered by this index
        cnt = [[] for _ in range(n)]
        # Index of the first greater-or-equal element to the right
        pos = [n] * n
        # Decreasing monotonic stack
        st = []

        left = 0
        for right in range(n):
            # Maintain the monotonic stack
            while st and nums[right] >= nums[st[-1]]:
                pos[st[-1]] = right
                st.pop()
            # The stack top is the nearest greater element to the left of nums[right]
            if st:
                cnt[st[-1]].append(right)
            st.append(right)

            # The priority queue front is the window maximum
            heapq.heappush(q, (-nums[right], right))
            # Adding nums[right] increases the operation count
            operations += max(0, -q[0][0] - nums[right])

            # The minimum operation count exceeds k; shrink the window
            while operations > k:
                # Removing nums[left] from the window decreases the operation count
                for i in cnt[left]:
                    # Subtract the contribution
                    operations -= (nums[left] - nums[i]) * (
                        min(pos[i], right + 1) - i
                    )
                left += 1

            # Remove elements with indices less than left from the priority queue
            while q and q[0][1] < left:
                heapq.heappop(q)

            # There are right - left + 1 valid contiguous subarrays ending at right
            ans += right - left + 1

        return ans