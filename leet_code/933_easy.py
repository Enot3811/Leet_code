
class RecentCounter:

    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)
        search = t - 3000
        if search <= 0:
            return len(self.requests)
        else:
            idx = self.binary_search(search)
            self.requests = self.requests[idx:]
            return len(self.requests[idx:])
        

    def binary_search(self, search: int):
        mid = len(self.requests) // 2
        left = 0
        right = len(self.requests) - 1
        while left <= right:
            if search == self.requests[mid]:
                return mid
            elif search < self.requests[mid]:
                right = mid - 1
            else:
                left = mid + 1
            mid = (right + left) // 2
        return mid + 1


# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
print(obj.ping(1))
print(obj.ping(100))
print(obj.ping(3001))
print(obj.ping(3002))
print(obj.ping(3003))
