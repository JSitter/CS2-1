from priorityqueue import PriorityQueue, PriorityNode

def test_instance():
  pq = PriorityQueue()
  assert pq.heap

def test_single_enqueue():
  pq = PriorityQueue()
  pq.enqueue(45, 3)
  assert pq.heap.items[0].value == 45
  assert pq.heap.items[0].priority == 3

def test_dequeue():
  pq = PriorityQueue()
  pq.enqueue(45, 3)
  assert pq.dequeue().value == 45

def test_multi_enqueue():
  pq = PriorityQueue()
  pq.enqueue(45, 3)
  pq.enqueue(50, 2)
  pq.enqueue(2, 1)
  pq.enqueue(34, 5)
  assert pq.heap.items[0].value == 2
  assert pq.dequeue().value == 2
  assert pq.dequeue().value == 50
  assert pq.dequeue().value == 45
  assert pq.dequeue().value == 34


