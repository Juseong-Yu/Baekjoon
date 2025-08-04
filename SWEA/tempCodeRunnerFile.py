    if heap[brother] < heap[idx]:
                        tmp = heap[brother]
                        heap[brother] = heap[idx]
                        heap[idx] = tmp
                        break