import java.io.*;
import java.util.*;

/*
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Group them-> {"paper, title"}, {"egg","add"},{"hello","billy"}
*/

public class Solution {
  
  public static List<List<String>> Group(String[] strs) {
    List<List<String>> ret = new ArrayList<>();
    HashMap<String, List<String>> map = new HashMap<>();
    for(String s : strs) {
      String key = hash(s);
      if(!map.containsKey(key)) {
        map.put(key,new ArrayList<String>());
      }
        map.get(key).add(s);
    }
    for(String key : map.keySet()) {
      ret.add(map.get(key));
    }
    return ret;
    
}
  
  public static String hash(String str) {
    HashMap<Character, Integer > map = new HashMap<>();
    StringBuilder sb = new StringBuilder();
    int cnt = 0;
    for(int i = 0;i<str.length();i++) {
      char c =str.charAt(i);
      if(!map.containsKey(c)) {
        sb.append(cnt+"#");
        map.put(c,cnt);
        cnt++;
      } else {
        sb.append(map.get(c)+"#");
      }
    }
    return sb.toString();
  }

  public static void main(String[] args) {
    String[] b ={"egg","add","laa","title","paper","hello","billy","kitten","how","today"};
    for(List<String> list : Group(b)) {
      for(String each : list) {
        System.out.print(each + " ");
      }
      System.out.println();
    }
    
  }
  
  
}
