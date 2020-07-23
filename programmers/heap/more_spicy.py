'''
문제 설명
매운 것을 좋아하는 Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶습니다. 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 Leo는 스코빌 지수가 가장 낮은 두 개의 음식을 아래와 같이 특별한 방법으로 섞어 새로운 음식을 만듭니다.

섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.
Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때, 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 solution 함수를 작성해주세요.

제한 사항
scoville의 길이는 2 이상 1,000,000 이하입니다.
K는 0 이상 1,000,000,000 이하입니다.
scoville의 원소는 각각 0 이상 1,000,000 이하입니다.
모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.
입출력 예
scoville	K	return
[1, 2, 3, 9, 10, 12]	7	2
입출력 예 설명
스코빌 지수가 1인 음식과 2인 음식을 섞으면 음식의 스코빌 지수가 아래와 같이 됩니다.
새로운 음식의 스코빌 지수 = 1 + (2 * 2) = 5
가진 음식의 스코빌 지수 = [5, 3, 9, 10, 12]

스코빌 지수가 3인 음식과 5인 음식을 섞으면 음식의 스코빌 지수가 아래와 같이 됩니다.
새로운 음식의 스코빌 지수 = 3 + (5 * 2) = 13
가진 음식의 스코빌 지수 = [13, 9, 10, 12]

모든 음식의 스코빌 지수가 7 이상이 되었고 이때 섞은 횟수는 2회입니다.
'''


class MinHeap:
    def __init__(self, arr):
        self.heap_array = []
        if arr is not None and type(arr) == list:
            self.heap_array.append(None)
            self.heap_array += arr
            self.heapify()

    def heapify(self):
        if len(self.heap_array) - 1 <= 1:
            return
        for i in reversed(range(1, len(self.heap_array))):
            self.move_down(self.heap_array, i)

    def move_down(self, heap_array, parent_idx):
        heap_size = len(heap_array) - 1
        left_idx = parent_idx * 2
        right_idx = parent_idx * 2 + 1
        largest_idx = parent_idx

        if left_idx <= heap_size and heap_array[largest_idx] > heap_array[left_idx]:
            largest_idx = left_idx
        if right_idx <= heap_size and heap_array[largest_idx] > heap_array[right_idx]:
            largest_idx = right_idx

        if largest_idx != parent_idx:
            heap_array[largest_idx], heap_array[parent_idx] = heap_array[parent_idx], heap_array[largest_idx]
            self.move_down(heap_array, largest_idx)

    def move_up(self, heap_array, child_idx):
        if child_idx <= 1:
            return
        parent_idx = child_idx // 2
        if heap_array[child_idx] < heap_array[parent_idx]:
            heap_array[child_idx], heap_array[parent_idx] = heap_array[parent_idx], heap_array[child_idx]
            self.move_up(heap_array, parent_idx)

    def push(self, data):
        if len(self.heap_array) == 0:
            self.heap_array.append(None)
            self.heap_array.append(data)
            return

        self.heap_array.append(data)
        self.move_up(self.heap_array, len(self.heap_array)-1)

    def pop(self):
        if len(self.heap_array) <= 1:
            return None
        elif len(self.heap_array) == 2:
            return self.heap_array.pop()
        heap_size = self.heap_size()
        self.heap_array[1], self.heap_array[heap_size] = self.heap_array[heap_size], self.heap_array[1]
        data = self.heap_array.pop()
        self.move_down(self.heap_array, 1)
        return data   

    def heap_size(self):
        return len(self.heap_array) - 1    

def solution(scoville, K):
    answer = 0
    heap = MinHeap(scoville)
    while True:
        if heap.heap_size() == 0:
            return -1

        min1 = heap.pop()
        if min1 >= K:
            break

        if heap.heap_size() == 0:
            return -1

        min2 = heap.pop()
        heap.push(min1 + min2 * 2)

        answer += 1
    return answer    

if __name__ == '__main__':
    assert solution([1, 2, 3, 9, 10, 12], 7) == 2
    assert solution([7, 2], 7) == 1
    assert solution([7, 2, 5], 7) == 1
    assert solution([1, 1], 7) == -1
    assert solution([12, 3, 10, 9, 1, 2], 7) == 2