#!/usr/local/bin/python

from tree import Node, Attribute, Leaf

class Edge :
	def __init__(self, node, cluster) :
		self.node = node
		self.cluster = cluster
		
	def __eq__(self, other) :
		return (sef.node == sef.node) and (self.cluster == other.cluster)
		
	def __hash__(self) :
		return hash(sef.node) + hash(self.cluster)
		
	def __repr__(self) :
		return repr((self.node, self.cluster))
	

def filter_edges_with_node(edge_list, node) :
	return [edge for edge in edge_list if edge.node == node]

def filter_edges_with_cluster(edge_list, cluster) :
	return [edge for edge in edge_list if edge.cluster == cluster]

def build_edge_list_from_node(node) :
	edge_list = []
	for child in node.children :
		if isinstance(child, Attribute) :
			for cluster in child.wrappers :
				edge_list.append(Edge(child.name, cluster))
		elif  isinstance(child, Node) :
			edge_list.extend(build_edge_list_from_node(child))
		
	return edge_list
	
def update_cluster_path(cluster, edge_list_of_cluster, node_list, cluster_ancestor_of_node) :
	for edge in edge_list_of_cluster :
		if edge.node not in cluster_ancestor_of_node :
			cluster_ancestor_of_node[edge.node] = cluster
			
			node_list.append(edge.node)
			
def update_node_path(edge_list, cluster_list, node_list, node_ancestor_of_cluster) :
	for node in node_list :
		edge_list_of_node = filter_edges_with_node(edge_list, node)
		
		for edge in edge_list_of_node :
			if edge.cluster not in node_ancestor_of_cluster :
				node_ancestor_of_cluster[edge.cluster] = edge.node
				cluster_list.append(edge.cluster)
				

def build_join_lists(cluster_start, cluster_end, node_ancestor_of_cluster, cluster_ancestor_of_node) :
	join_cluster_list = [cluster_end]
	join_node_list = []
	cluster_it = cluster_end
	node_it = None
	
	eureka = False
	
	while not eureka :
		node_it = node_ancestor_of_cluster[cluster_it]
		join_node_list.append(node_it)
		
		cluster_it = cluster_ancestor_of_node[node_it]
		
		if cluster_it == cluster_start :
			eureka = True
		
		join_cluster_list.append(cluster_it)
			
	return join_cluster_list, join_node_list
				
def find_join_path(root, tree1, tree2) :
	edge_list = build_edge_list_from_node(root)
	
	cluster_start = tree1.wrappers[0]
	cluster_end   = tree2.wrappers[0]
	
	cluster_list  = [cluster_start]
	node_list     = []
	
	cluster_ancestor_of_node = dict() # node -> cluster
	node_ancestor_of_cluster = dict() # cluster -> node
	
	while not len(cluster_list) > 0 :
		cluster = cluster_list.pop()
		edge_list_of_cluster = filter_edges_with_cluster(edge_list, cluster)
		
		update_cluster_path(cluster, edge_list_of_cluster, node_list, cluster_ancestor_of_node)
		update_node_path(edge_list, cluster_list, node_list, node_ancestor_of_cluster)
		
	(join_cluster_list, join_node_list) = build_join_lists(cluster_start, cluster_end, node_ancestor_of_cluster, cluster_ancestor_of_node)
		
	return (join_cluster_list, join_node_list)
		
# edge_list = [Edge("A", "a"),Edge("A", "b"),Edge("B", "b"),Edge("B", "c"),Edge("C", "a")]
# print(filter_edges_with_cluster(edge_list, "a"))

# node_list = []
# cluster_ancestor_of_node = dict()
# edge_list_of_cluster = [Edge("A", "a"),Edge("C", "a")]
# update_cluster_path(cluster, edge_list_of_cluster, node_list, cluster_ancestor_of_node)
# print(node_list)

# edge_list = [Edge("A", "a"),Edge("A", "b"),Edge("B", "b"),Edge("B", "c"),Edge("C", "a")]
# node_list = ["A"]
# cluster_list = []
# node_ancestor_of_cluster = dict()
# update_node_path(edge_list, cluster_list, node_list, node_ancestor_of_cluster)
# print(cluster_list)

# cluster_start = "A"
# cluster_end   = "D"
# node_ancestor_of_cluster = dict([("B", "a"),("C", "b"),("D", "b")])
# cluster_ancestor_of_node = dict([("a", "A"),("b", "B"),("c", "D")])
# (join_cluster_list, join_node_list) = build_join_lists(cluster_start, cluster_end, node_ancestor_of_cluster, cluster_ancestor_of_node)
# print(join_cluster_list)
# print(join_node_list)

#edge_list = build_edge_list_from_node(pokemonPokedex)
