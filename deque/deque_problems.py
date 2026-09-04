#problem no: 933
#time complexity: O(n)
#space complexity: O(n)

from collections import deque

class RecentCounter:

    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        self.q.append(t)

        while self.q[0] < t - 3000:
            self.q.popleft()

        return len(self.q)
        



#problem no: 649
#time complexity: O(n)
#space complexity: O(n)
from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)

        r = deque()
        d = deque()

        for i in range(n):
            if senate[i] == 'R':
                r.append(i)
            else:
                d.append(i)

        while r and d:
            ri = r.popleft()
            di = d.popleft()

            if ri < di:
                r.append(ri + n)
            else:
                d.append(di + n)

        return "Radiant" if r else "Dire"