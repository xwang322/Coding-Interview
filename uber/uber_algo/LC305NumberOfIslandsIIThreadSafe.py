import threading
class Solution(object):
    def __init__(self):
        self.lock = threading.Lock()

    def numIslands2(self, m, n, positions):
        if not m or not n or not positions:
            return []
        answer = []
        parent = [[(-1, -1) for i in range(n)] for j in range(m)]
        directions = [(-1, 0),(1, 0),(0, 1),(0, -1)]
        num = 0
        for row, col in positions:
            self.lock.acquire()
            print 'A'
            parent[row][col] = (row, col)
            num += 1
            for direction in directions:
                row_now = row+direction[0]
                col_now = col+direction[1]
                if row_now < 0 or row_now >= m or col_now < 0 or col_now >= n or parent[row_now][col_now]==(-1, -1):
                    continue
                if not self.union(row, col, row_now, col_now, parent):
                    num -= 1
            answer.append(num)
            self.lock.release()
        return answer

    def union(self, row, col, row_now, col_now, parent):
        root1 = self.find(row, col, parent)
        root2 = self.find(row_now, col_now, parent)
        if root1 == root2:
            return True
        parent[root1[0]][root1[1]] = (root2[0], root2[1])
        return False

    def find(self, row, col, parent):
        if not (row == parent[row][col][0] and col == parent[row][col][1]):
            parent[row][col] = self.find(parent[row][col][0], parent[row][col][1], parent)
        return parent[row][col]

def worker1(s):
    s.numIslands2(3,3,[[0,0],[0,1]])

def worker2(s):
    s.numIslands2(3,3,[[1,2],[2,1]])

process = Solution()
threads = []
for worker in [worker1, worker2]:
    threads.append(threading.Thread(target = worker, args = (process,)))
    threads[-1].start()
main_thread = threading.currentThread()
for thread in threads:
    if thread is not main_thread:
        thread.join()
