class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        if not candidates or not target:
            return None
        result = []
        def helper(start_idx, target: int, current_state: list[int]) -> list[list[int]]:
            # termination condition
            # base case 1
            if target == 0:
                result.append(list(current_state))
                return
            # base case 2
            if target < 0:
                return

            for i in range(start_idx, len(candidates)):
                candidate = candidates[i]
                # update current state
                current_state.append(candidate)
                # recursive dfs on updated state
                helper(i, target - candidate, current_state)
                # backtrack
                current_state.pop()
        
        helper(0, target, [])
        return result


        

                