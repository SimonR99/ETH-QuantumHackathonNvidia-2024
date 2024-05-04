from itertools import permutations

def brute_force_tsp(w, N, debug = False):
    a = list(permutations(range(1, N)))
    last_best_distance = 1e10
    for i in a:
        distance = 0
        pre_j = 0
        for j in i:
            distance = distance + w[j, pre_j]
            pre_j = j
        distance = distance + w[pre_j, 0]
        order = (0,) + i
        if distance < last_best_distance:
            best_order = order
            last_best_distance = distance
            if debug:
                print("order = " + str(order) + " Distance = " + str(distance))
    return last_best_distance, best_order