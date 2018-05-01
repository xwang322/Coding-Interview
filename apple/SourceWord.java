// 给一个string source, 比如 "aabcf"， 给一个list of word, 求list里面可以用source组成的word
import java.util.*;
import java.io.*;
class Solution {
    public static void main(String[] args) {
        List<String> question = new ArrayList<>();
        question.add("aabc");
        question.add("aabce");
        question.add("a");
        question.add("");
        List<String> answer = SourceWord(new String("aabcf"), question);
        for (String each : answer) {
            System.out.println(each);
        }
    }

    public static List<String> SourceWord(String str, List<String> words) {
        List<String> answer = new ArrayList<>();
        if (str == null  || words == null) return answer;
        HashMap<Character, Integer> hm = new HashMap<>();
        for (int i = 0; i < str.length(); i++) {
            hm.put(str.charAt(i), hm.getOrDefault(str.charAt(i), 0)+1);
        }
        for (String word : words) {
            if (word == null) continue;
            HashMap<Character, Integer> temp = new HashMap<>();
            for (int i = 0; i < word.length(); i++) {
                if (!hm.containsKey(word.charAt(i))) break;
                temp.put(word.charAt(i), temp.getOrDefault(word.charAt(i), 0)+1);
                if (temp.get(word.charAt(i)) > hm.get(word.charAt(i))) break;
                if (i == word.length()-1) answer.add(word);
            }
        }
        return answer;
    }
 }

 // another easier way to save space
class Solution {
    public static void main(String[] args) {
        List<String> question = Arrays.asList(new String[]{"aabc","aabce","a",""});
        List<String> answer = SourceWord(new String("aabcf"), question);
        for (String each : answer) {
            System.out.println(each);
        }
    }

    public static List<String> SourceWord(String str, List<String> words) {
        List<String> answer = new ArrayList<>();
        if (str == null  || words == null) return answer;
        int[] chars = new int[256];
        for (int i = 0; i < str.length(); i++) {
            chars[(int)str.charAt(i)]++;
        }
        for (String word : words) {
            if (word == null) continue;
            int[] temp = new int[256];
            for (int i = 0; i < word.length(); i++) {
                temp[(int)word.charAt(i)]++;
            }
            if (diff(temp, chars)) answer.add(word);
        }
        return answer;
    }

    public static boolean diff(int[] a, int[] b) {
        for (int i = 0; i < 256; i++) {
            if (a[i] > b[i]) return false;
        }
        return true;
    }
 }
