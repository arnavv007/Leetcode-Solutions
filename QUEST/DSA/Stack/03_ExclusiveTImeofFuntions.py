class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        res = [0] * n
        stack = []
        prev_time = 0
        
        for log in logs:
            id_str, type, time_str = log.split(':')
            fn_id, timestamp = int(id_str), int(time_str)
            
            if type == "start":
                if stack:
                    res[stack[-1]] += timestamp - prev_time
               
                stack.append(fn_id)
              
                prev_time = timestamp
            else:
                top_id = stack.pop()
                res[top_id] += timestamp - prev_time + 1
                prev_time = timestamp + 1
                
        return res

print(Solution.exclusiveTime(Solution, ["0:start:0","1:start:2","1:end:5","0:end:6"]))