import java.io.*;
import java.util.*;

/*
 * To execute Java, please define "static void main" on a class
 * named Solution.
 *
 * If you need more classes, simply define them inline.
 */

class ListNode {
  String key;
  int val;
  ListNode next;
  public ListNode(String key, int val) {
    this.key = key;
    this.val  =val;
  }
}

class HashTable {
  
  static int default_cnt = 16;
  ListNode[] buckets;

  public HashTable(){
    buckets = new ListNode[default_cnt];
  }
  
  public int get(String key) {
    int hash = hash(key);
    int idx = getIdx(hash);
    //System.out.println(idx);
    if(buckets[idx] == null) {
      return -1;
    }
    
    ListNode head = buckets[idx];
   // System.out.println(head.key);
    while(head!= null && !head.key.equals(key)) {
      head = head.next;
    }
    return head==null? -1:head.val;
  }
  
  
  public void put(String key, int val) {
    int hash = hash(key);
    int idx = getIdx(hash);
    if(buckets[idx] == null) {
      buckets[idx] = new ListNode(key,val);
      return;
    }
    ListNode head = buckets[idx];
    while(head.next != null) {
      if(head.key.equals(key)) {
        head.val = val;
        return;
      }
    }
    ListNode newNode = new ListNode(key,val);
    newNode.next = head;
    buckets[idx] = newNode;
  }
  
  private static int hash(String key) {
   
    int hash = key.length();
    for(int i = 0; i < key.length(); i++)  
      {  
         hash = ((hash << 5) ^ (hash >> 27)) ^ key.charAt(i);  
      }  
      return hash;  
  }
  
  private static int getIdx(int hash) {
    return hash&(default_cnt -1);
  }
}

class Solution {
  
  
  public static void main(String[] args) {
    HashTable h = new HashTable();
    h.put("k",24);
    h.put("k",28);
    System.out.print(h.get("i"));
    System.out.print(h.get("z"));
  }
}


/* 
Your previous C++ content is preserved below:

//java 实现hashtable by linked list


 */