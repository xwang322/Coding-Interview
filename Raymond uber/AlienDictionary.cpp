#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
using namespace std;
class Solution {
    unordered_map<char, vector<char> >adj;
    unordered_map<char, bool>visited;
    unordered_set<char>current;
    string res="";
public:
   bool Tsort(char ch) {
    if (current.count(ch)) return false;
    if (visited[ch]) return true;
    visited[ch]=true;
    current.insert(ch);

    for (auto & letter : adj[ch])if (Tsort(letter) == false)return false;

    current.erase(ch);
    res= ch + res;

    return true;
}
void  MissMatch(string s1, string s2){
    bool miss=false;
        for (int i = 0; i < max(s1.length(), s2.length()); i++) {
            if (i < s1.length() && adj.find(s1[i]) ==adj.end())
               adj[s1[i]]={}; 
                
            if (i < s2.length() && adj.find(s2[i]) == adj.end())
                adj[s2[i]]={};
                
            if (i < min(s1.length(), s2.length()) && s1[i] != s2[i] && !miss) {
               adj[s1[i]].push_back(s2[i]);
               miss=true;
            }
        }
}
string alienOrder(vector<string>& words) {
    if (words.size() == 1) return words[0];

    for (int i = 0; i < words.size()-1; i++) {
        string s1 = words[i];
        string s2 = words[i + 1];           
        MissMatch(s1, s2);
    }

    for (auto & v : adj)
        if (Tsort(v.first) == false)return "";
    cout << res << endl;
    return res;
    
    }
};
int main()
{
    Solution s;
    vector<string>words={"wrt","wrf", "er","ett", "rftt"};
    s.alienOrder(words);

    
    return 0;
}