import time


def can_finish_with_leftovers(manager, time_needed):
    for j in range(len(manager.time_left)):
        manager.time_left[j] -= time_needed
        if manager.time_left[j] == 0:
            manager.time_left.pop(j)
            manager.processors.pop(j)
    time.sleep(time_needed)


def need_to_buy_more_processors(manager, to_buy, time_left, i):
    for j in range(len(manager.time_left)):
        manager.time_left[j] -= manager.time_left[i]
    time_left -= manager.time_left[i]
    current_processors = manager.processors
    manager.time_left.pop(i)
    manager.processors.pop(i)
    manager.time_left.append(60)
    manager.processors.append(current_processors)
    to_buy += current_processors
    time.sleep(manager.time_left[i])
