OUTER_ITER_LIMIT = 100
INNER_ITER_LIMIT = 100
def transfert_node(node,cluster1, cluster2, weight_limit):
    if node in cluster1.nodes():
        node_data = cluster1.nodes[node]
        cluster2.add_node(node, **node_data)
        cluster1.remove_node(node)
        if sum(nx.get_node_attributes(cluster2, 'weight')) > weight_limit:
            cluster1.add_node(node, **node_data)
            cluster2.remove_node(node)

for count, cluster in enumerate(Cluster_list):
    if len(Cluster_list)-1 <= count+1 or OUTER_ITER_LIMIT < count:
        break
    cluster_2 = Cluster_list[count+1]
    ii = 0
    ref_cluster = cluster.copy()
    for node in ref_cluster:
        if ii >= INNER_ITER_LIMIT:
            break
        transfert_node(node,cluster, cluster_2,C) # transfert node to cluster 2 and check if it's below weights limit
        print("supge")
        cc_mj = CC(cluster_2)
        cc_mk = CC(cluster)
        if (cc_mj < cc_mk):
            continue
        else:
            transfert_node(node, cluster_2, cluster,C)
        ii += 1

    CC(cluster)