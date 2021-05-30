import sys

while True:
    stack = []
    queue = []
    priorityqueue = []

    try:
        vezes = int(input())
        stack_count, queue_count, pq_count = True, True, True

        for x in range(vezes):
            a, b = list(map(int, input().split()))
            if a == 1:
                stack.append(b)
                queue.append(b)
                priorityqueue.append(b)
            else:
                if b != stack.pop(-1):
                    stack_count = False
                if b != queue.pop(0):
                    queue_count = False
                valor = priorityqueue.index(max(priorityqueue))
                if b != priorityqueue.pop(valor):
                    pq_count = False

        if (queue_count and pq_count) or (queue_count and stack_count) or (pq_count and stack_count):
            print("not sure")
        elif not stack_count and not queue_count and not pq_count:
            print("impossible")
        elif stack_count:
            print("stack")
        elif queue_count:
            print("queue")
        elif pq_count:
            print("priority queue")

    except EOFError:
        sys.exit()
