# optimisation step
OUTER_ITER_LIMIT = 100
INNER_ITER_LIMIT = 100
for count, cluster in enumerate(Cluster_list):
    if len(Cluster_list)-1 <= count+1 or OUTER_ITER_LIMIT < count:
        break
    cluster_2 = Cluster_list[count+1]
    ii = 0
    for node in cluster:
        if ii >= INNER_ITER_LIMIT:
            break
        cluster_2 = tranfert_node(node,cluster_2) # check if it's below weights limit
        cc_mj = CC(cluster_2)
        cc_mk = CC(cluster)
        if (cc_mj < cc_mk):
            continue
        else:
            transfert_node(cluster_2, node)
        ii += 1

    CC(cluster)
