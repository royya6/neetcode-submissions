class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        road = [(position[i], speed[i]) for i in range(n)]
        road.sort(key= lambda x: x[0], reverse=True)

        # time a car arrives at target
        def arrival(position: int, speed: int) -> int: 
            return (target - position) / speed 

        # arrival times 
        stack = [arrival(road[0][0], road[0][1])]
        print(stack)

        for i in range(1, n): 
            stack.append(arrival(road[i][0], road[i][1]))
            if stack and stack[-1] <= stack[-2]: 
                stack.pop()

        return len(stack)
        