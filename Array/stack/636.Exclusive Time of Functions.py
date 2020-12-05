class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []
        prev_time = 0
        for log in logs:
            f_id, f_type, time = log.split(':')
            f_id, time = int(f_id), int(time)
            if f_type == 'start':
                if stack:
                    res[stack[-1]] += time - prev_time
                stack.append(f_id)
                prev_time = time
            else:
                res[stack.pop()] += time - prev_time + 1
                prev_time = time + 1
                
        return res
                