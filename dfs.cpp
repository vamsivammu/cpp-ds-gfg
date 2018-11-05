#include<iostream>
#include<iterator>
#include<list>
#include<utility>
using namespace std;
class Graph
{
    int numvert;
    list<int> *adj;
    public:
        Graph(int V);
        void addedge(int u,int w);
        void dfsutil(int v,bool vis[]);
        void dfs(int s);

};

Graph::Graph(int V){
    this->numvert = V;
    adj = new list<int>[V];

}

void Graph::addedge(int u,int w){
    adj[u].push_back(w);

}

void Graph::dfsutil(int v,bool vis[]){
    vis[v]=true;
    cout<<v<<" ";
    list<int>::iterator it;
    for(it=adj[v].begin();it!=adj[v].end();++it){
        if(!vis[*it]){
            dfsutil(*it,vis);
        }
    }
}
void Graph::dfs(int s){
    bool *vis = new bool[numvert];
    for(int i = 0;i<numvert;i++){
        vis[i]=false;
    }
    dfsutil(s,vis);
}
int main()
{
    // Create a graph given in the above diagram
    Graph g(4);
    g.addedge(0, 1);
    g.addedge(0, 2);
    g.addedge(1, 2);
    g.addedge(2, 0);
    g.addedge(2, 3);
    g.addedge(3, 3);
 
    cout << "Following is Depth First Traversal"
            " (starting from vertex 2) \n";
    g.dfs(2);
 
    return 0;
}