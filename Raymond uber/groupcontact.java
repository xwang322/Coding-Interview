import java.io.*;
import java.util.*;

//program to find same contacts in a list of contacts

//union find!但是不能确定bucket的数量，所以全部用hashmap来代替arr，主要函数，findroot， union， find group, 想象一张图里有很多点的概念

class Solution {
  
  public static void group(HashMap<Integer,String[]> contact) {
    int len = contact.size();
    int[] roots = new int[len];
    HashMap<String,Integer> map = new HashMap<>();
    for(int i=0;i<len;i++) {
      roots[i] = i;
    }
    // union
    for(int person : contact.keySet()) {
      int curRoot = person; // very important
      String[] emails = contact.get(person);
      for(String email : emails) {
        if(map.containsKey(email)) {
          int root = getRoot(map.get(email),roots);
          roots[person] = root;
          if(root!= curRoot) {    // very important!!前后成环现象
            roots[curRoot] = root;
            curRoot = root;
          }
          
        } else {
          map.put(email,person);
        }  
      }
    }
    
    List<List<Integer>> ret = new ArrayList<>();
    HashMap<Integer,List<Integer>> tmpmap = new HashMap<>();
    //HashSet<Integer> set = new HashSet<>();
    for(int i=0;i<roots.length;i++) {
      if(tmpmap.containsKey(getRoot(i,roots))) {
        
      } else {
        tmpmap.put(getRoot(i,roots),new ArrayList<>());
      } 
      tmpmap.get(getRoot(i,roots)).add(i);
    }
    for(int i=0;i<roots.length;i++) {
      System.out.print(roots[i]);
      
    }
    System.out.println();
    for(Integer key : tmpmap.keySet()) {
      List<Integer> list = tmpmap.get(key);
      for(Integer each: list) {
        System.out.print(each+" ");
      }
      System.out.println();
    }
  }
  
  public static int getRoot(int i, int[] roots) {
    while(roots[i] != i) {
      i = roots[i];
    }
    return i;
  }
  
  
  public static void main(String[] args) {
    HashMap<Integer,String[]> map = new HashMap<>();
    String[][] ss = {{"Gaurav", "gaurav@gmail.com", "gaurav@gfgQA.com"},{"Lucky", "lucky@gmail.com", "+1234567"},{"gaurav123", "+5412312", "gaurav123@skype.com"},{"gaurav1993", "+5412312", "gaurav@gfgQA.com"},{"raja", "+2231210", "raja@gfg.com"},{"bahubali", "+878312", "raja"}};

    for(int i=0;i<6;i++) { 
      map.put(i,ss[i]);
    }
    group(map);
  }
  
  
}

