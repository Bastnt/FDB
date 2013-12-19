#!/usr/local/bin/python
    
class Edge :
  def __init__(self, concept, source, value) :
    self.concept = concept
    self.source = source
    self.value = value
    
  def match_source(self, source) :
    return self.source == source
    
  def __eq__(self, other) :
    return (self.concept == other.concept) and (self.source == other.source)
    
  def __hash__(self) :
    return hash(self.concept) + hash(self.source)

  def __repr__(self) :
    return self.concept, self.source, self.value
    
class Match :
  def __init__(self, source1, value1, source2, value2) :
    self.source1
    self.value1
    self.source2
    self.value2
    
  def __repr__(self) :
    return self.source1, self.value1, self.source2, self.value2
	

class MatchingGraph :
  edges = []
  
  def add_edge(self, concept, source, value) :
    self.edges.append(Edge(concept, source, value))
  
  def filter_by_source(self, source) :
    images = [edge for edge in self.edges if edge.match_source(source)]
    return set(images)
    
  def find_match(self, source1, source2) :
    edge_set1 = self.filter_by_source(source1)
    edge_set2 = self.filter_by_source(source2)
    edge_set = {edge for egde in edge_set1 ^ edge_set2}
    
    match_list = []
    for edge1 in edge_set1 :
      for edge2 in edge_set2 :
        if edge1.source == edge2.source :
          match_list.append(Match(edge1.source, edge1.value, edge2.source, edge2.value))
    
    return match_list
    
mg = MatchingGraph()
mg.add_edge("a", "A", "Aa")
mg.add_edge("b", "A", "Ab")
mg.add_edge("b", "B", "Bb")
mg.add_edge("c", "B", "Bc")
print mg.find_match("A", "B")[0].value1


#!/usr/local/bin/python2.7
    
class Edge :
  def __init__(self, concept, source, value) :
    self.concept = concept
    self.source = source
    self.value = value
    
  def match_source(self, source) :
    return self.source == source
    
  def __eq__(self, other) :
    return (self.concept == other.concept) and (self.source == other.source)
    
  def __hash__(self) :
    return hash(self.concept) + hash(self.source)

  def __repr__(self) :
    return repr((self.concept, self.source, self.value))
    
class Match :
  def __init__(self, source1, value1, source2, value2) :
    self.source1 = source1
    self.value1  = value1
    self.source2 = source2
    self.value2  = value2
    
  def __repr__(self) :
    return repr((self.source1, self.value1, self.source2, self.value2))
  

class MatchingGraph :
  edges = []
  
  def add_edge(self, concept, source, value) :
    self.edges.append(Edge(concept, source, value))
  
  def filter_by_source(self, source) :
    images = [edge for edge in self.edges if edge.match_source(source)]
    return set(images)
    
  def find_match(self, source1, source2) :
    edge_set1 = self.filter_by_source(source1)
    edge_set2 = self.filter_by_source(source2)
    edge_set = {edge for edge in edge_set1 ^ edge_set2}
    
    print edge_set1
    print edge_set2
    
    match_list = []
    for edge1 in edge_set1 :
      for edge2 in edge_set2 :
        if edge1.concept == edge2.concept :
          match_list.append(Match(edge1.source, edge1.value, edge2.source, edge2.value))
    
    return match_list
    
mg = MatchingGraph()
mg.add_edge("a", "A", "Aa")
mg.add_edge("b", "A", "Ab")
mg.add_edge("b", "B", "Bb")
mg.add_edge("c", "B", "Bc")
print mg.find_match("A", "B")
    
# set([('a', 'A', 'Aa'), ('b', 'A', 'Ab')])
# set([('c', 'B', 'Bc'), ('b', 'B', 'Bb')])
# [('A', 'Ab', 'B', 'Bb')]