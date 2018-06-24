/*
deep copy graph.
DFS or BFS, too lazy to write test case
*/
 struct UndirectedGraphNode {
      int label;
      vector<UndirectedGraphNode *> neighbors;
      UndirectedGraphNode(int x) : label(x) {};
 };
 
class Solution {
typedef UndirectedGraphNode graph;
private:
    unordered_map<graph *, graph *>map;
    queue<graph *>Q;
public:
    graph * BFS_cloneGraph(graph *node) {
        if(!node)return NULL;
        graph * newhead= new graph(node->label);
        map[node]=newhead;
        Q.push(node);
        
        while(!Q.empty()){
            graph * cur=Q.front();
            Q.pop();
            vector<graph *>neighbor=cur->neighbors;
            for(auto & b : neighbor){
                if(map.find(b)==map.end()){
                    graph * copy =new graph(b->label);
                    map[b]=copy;
                    map[cur]->neighbors.push_back(copy);
                    Q.push(b);
                }
                else map[cur]->neighbors.push_back(map[b]);
            }
        }
        return newhead;
    }
};


//dfs

typedef UndirectedGraphNode graph;
class Solution {
private:
	unordered_map<graph*, graph*> map;
public:
    graph *cloneGraph(graph *node) {
        if(!node)  return node;
        auto iter = map.find(node);
        if(iter==map.end()){
          
            graph* copy = new graph(node->label);
            map[node] = copy;
            for(int i=0; i<node->neighbors.size(); i++)
                copy->neighbors.push_back(cloneGraph(node->neighbors[i]));
            return copy;
        }
        else return iter->second;
    }
};