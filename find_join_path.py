#!/usr/local/bin/python

from tree import Node, Tree, Leaf

class Edge :
	def _init(self, leaf, cluster) :
		self.leaf = leaf
		self.cluster = cluster
		
	def __eq__(self, other) :
		return (self.leaf == self.leaf) and (self.cluster == other.cluster)
		
	def __hash__(self) :
		return hash(self.leaf) + hash(self.cluster)
	

def filter_edges_with_node(edge_list, node) :
	return [edge for edge in edge_list if edge.node == node]

def filter_edges_with_cluster(edge_list, cluster) :
	return [edge for edge in edge_list if edge.cluster == cluster]

def build_edge_list_from_node(node) :
	edge_list = []
	for child in node.children :
		if  isinstance(child, Leaf) :
			edge_list.extend(child.attributes)
		else :
			edge.list.extend(build_edge_list_from_node(child))
			
	return edge_list
	
	
def find_join_path(root, tree1, tree2) :
	edge_list = build_edge_list_from_node(root)
	
	cluster_start = tree1.attributes[0]
	cluster_end   = tree2.attributes[0]
	
	cluster_list  = cluster_start
	node_list     = []
	
	cluster_ancestor_of_node = dict() # node -> cluster
	node_ancestor_of_cluster = dict() # cluster -> node
	
	while not len(cluster_list) > 0 :
		
		cluster = cluster_list.pop()
		
		edge_list_of_cluster = filter_edges_with_cluster(edge_list, cluster)
		
		for edge in edge_list_of_cluster :
			if edge.node not in cluster_ancestor_of_node :
				cluster_ancestor_of_node[edge.node] = cluster
				
				node_list.append(edge.node)
				
		for node in node_list :
			edge_list_of_node = filter_edges_with_node(edge_list, node)
			
			for edge in edge_list_of_node :
				if edge.cluster not in node_ancestor_of_cluster :
					node_ancestor_of_cluster[edge.cluster] = edge.node
					
					cluster_list.append(edge.cluster)
		
	join_cluster_list = [cluster.end]
	join_node_list = []
	cluster_it = cluster.end
	node_it = None
	
	eureka = False
	
	while not eureka :
		node_it = node_ancestor_of_cluster(cluster_it)
		join_node_list.append(node_it)
		
		cluster_it = cluster_ancestor_of_node(node_it)
		
		if cluster_it == cluster_start :
			eureka = True
		else :
			join_cluster_list.append(cluster_it)
		
	return (join_cluster_list, join_node_list)
		
	