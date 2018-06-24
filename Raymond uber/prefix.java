

/*
给了一个string的list，让给出所有可以成为除自己以外的prefix的string。
例如["a", "ab", "dogcat","dog"]，就返回"a"和"dog"
*/
//主要任务，建立Trie Tree, 定义有点奇怪，也可以先排序

import java.io.*;
import java.util.*;

class TrieNode {
  boolean end;
  TrieNode[] list;
  public TrieNode() {
    end = false;
    list = new TrieNode[26];
  }
  
  public TrieNode get(char c) {
    return list[c-'a'];
  }
  
  public boolean isEnd() {
    return end;
  }
  
  public void setEnd(boolean b) {
    end = b;
  }
  
  public boolean contains(char c) {
    return list[c-'a'] != null;
  }
  
  public void put(char c) {
    list[c-'a'] = new TrieNode();
  }
}


class Solution {
  TrieNode root = new TrieNode(); 
  
  public List<String> prefix(String[] strs) {
    
    Arrays.sort(strs);
    List<String > ret = new ArrayList<>();
    boolean flag = true;
    for(String str : strs) {
      TrieNode root = this.root;
      flag = true;
      for(char c : str.toCharArray()) {
        
        if(root.contains(c)) {
          if(root.get(c).isEnd()) {
            flag = false;
            break;
          }  
        } else {
          root.put(c);
        }
        root = root.get(c);
      }
      if(flag) {
        ret.add(str);
        root.setEnd(true);
      }
      
    }
    return ret;
  }   

  public static void main(String[] args) {
    Solution s = new Solution();
    String[] strs ={"a","ab","dogcat","dog", "hello","he"};
    for(String each : s.prefix(strs)) {
      System.out.print(each +" ");
    } 
  }
}
