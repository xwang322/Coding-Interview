/*
判断一个字符串里没有重复字符
*/
import java.io.*;
import java.util.*;
class Solution {
    public static void main (String[] args) {
        Boolean answer = Duplicates(new String("aab"));
        System.out.println(answer);
    }
    public static Boolean Duplicates(String str) {
        if (str == null) return true;
        Set<Character> set = new HashSet<>();
        for (int i = 0; i < str.length(); i++) {
            char temp = str.charAt(i);
            if (set.add(temp) == false) return false;
        }
        return true;
    }
}
