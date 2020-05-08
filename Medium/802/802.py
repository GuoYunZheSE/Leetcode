class Solution:
    def DFS(self,curr:int):
        if curr in self.final:
            return True
        else:
            return
    def eventualSafeNodes(self, graph: [[int]]) -> [int]:
        self.final=set()
        self.graph_dic={}
        for source,destination in enumerate(graph):
            self.graph_dic.setdefault(source,destination)
            if destination==[]:
                self.final.add(source)



