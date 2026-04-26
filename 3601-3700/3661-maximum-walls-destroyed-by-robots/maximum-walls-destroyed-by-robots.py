class Solution:
    def maxWalls(
        self, robots: List[int], distance: List[int], walls: List[int]
    ) -> int:
        n = len(robots)
        robot_dist = list(zip(robots, distance))
        robot_dist.sort(key=lambda x: x[0])
        walls.sort()

        m = len(walls)
        right_ptr = left_ptr = cur_ptr = robot_ptr = 0

        prev_left = prev_right = prev_num = 0
        sub_left = sub_right = 0

        for i in range(n):
            robot_pos, robot_dist_val = robot_dist[i]

            while right_ptr < m and walls[right_ptr] <= robot_pos:
                right_ptr += 1
            pos1 = right_ptr

            while cur_ptr < m and walls[cur_ptr] < robot_pos:
                cur_ptr += 1
            pos2 = cur_ptr

            if i >= 1:
                left_bound = max(
                    robot_pos - robot_dist_val, robot_dist[i - 1][0] + 1
                )
            else:
                left_bound = robot_pos - robot_dist_val

            while left_ptr < m and walls[left_ptr] < left_bound:
                left_ptr += 1
            left_pos = left_ptr
            current_left = pos1 - left_pos

            if i < n - 1:
                right_bound = min(
                    robot_pos + robot_dist_val, robot_dist[i + 1][0] - 1
                )
            else:
                right_bound = robot_pos + robot_dist_val

            while right_ptr < m and walls[right_ptr] <= right_bound:
                right_ptr += 1
            right_pos = right_ptr
            current_right = right_pos - pos2

            current_num = 0
            if i > 0:
                while robot_ptr < m and walls[robot_ptr] < robot_dist[i - 1][0]:
                    robot_ptr += 1
                pos3 = robot_ptr
                current_num = pos1 - pos3

            if i == 0:
                sub_left = current_left
                sub_right = current_right
            else:
                new_sub_left = max(
                    sub_left + current_left,
                    sub_right
                    - prev_right
                    + min(current_left + prev_right, current_num),
                )
                new_sub_right = max(
                    sub_left + current_right, sub_right + current_right
                )
                sub_left = new_sub_left
                sub_right = new_sub_right

            prev_left = current_left
            prev_right = current_right
            prev_num = current_num

        return max(sub_left, sub_right)