/*
给了一个string的list，让给出所有可以成为除自己以外的prefix的string。
例如["a", "ab", "dogcat","dog"]，就返回"a"和"dog"
*/
#include <vector>
#include <iostream>
#include <string>
using namespace std;
class TrieNode {
public:
    // Initialize your data structure here.
    bool end=false;
    vector<TrieNode*>list;
    void put(char ch, TrieNode * node){
        list[ch-'a']=node;
    }
    void setEnd(){
        end=true;
    }
    TrieNode * get(char ch){
        return list[ch-'a'];
    }
    bool contain(char ch){
        return list[ch-'a']!=NULL;
    }
    bool isEnd(){
        return end;
    }
    TrieNode() {
        list.resize(26);
    }
};

class Trie {
public:
    Trie() {
        root = new TrieNode();
    }

    // Inserts a word into the trie.
    void insert(string word) {
        TrieNode * node=root;
        for(int i=0; i < word.length(); i++){
            char ch=word[i];
            if(!node->contain(ch)){
                node->put(ch, new TrieNode());
            }
            node=node->get(ch);
        }
        node->setEnd();
    }

    // Returns if the word is in the trie.
    bool search(string word) {
        TrieNode * node=searchPrefix(word);
        return node!=NULL && node->isEnd();
    }

    // Returns if there is any word in the trie
    // that starts with the given prefix.
    bool startsWith(string prefix) {
        TrieNode * node=searchPrefix(prefix);
        return node!=NULL;
    }

private:
    TrieNode* root;
    
    TrieNode * searchPrefix(string word){
        TrieNode * node=root;
        for(int i=0; i < word.length(); i++){
            char ch=word[i];
            if(!node->contain(ch))return NULL;
            node=node->get(ch);
        }
        for(int i=0; i < 26; i++){
        	if(node->contain('a'+i))return node;
        }
        return NULL;
    }
};
int main(){
	Trie trie;
	string str[]={"a","ab","dogcat","dog", "hello","he"};
	vector<string>res;
	for(auto & s : str)trie.insert(s);

	for(auto & s : str){
		if(trie.startsWith(s)){
			// << s  << endl;//--------for test, in this case, it should output "a", "dog","he" 
			res.push_back(s);
		}
	}

	return 0;
}