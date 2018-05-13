/*
Stream
- getNextChar: Char
- isEndOfStream: Boolean
Once you hit end of stream, return first non-repeating word.
*/

import java.io.*;
import java.util.*;

class Solution {
  public static void main(String[] args) {
    //
  }

  public static String readSTream(Stream stream) {
      Map<String, Integer> hm = new LinkedHashMap<>();
      // use LinkedHashSet is even better, because we do not care about value in this case.
      Set<String> set = new HashSet<>();
      StringBuilder sb = new StringBuilder();
      int current = 0;
      while (!isEndOfStream(stream)) {
          char c = getNextChar(stream);
          if (c != ' ') {
              sb.append(c);
          } else {
              String str = new String(sb.toString());
              if (set.contains(str)) {
                  if (hm.get(str) != null) {
                      hm.remove(str);
                  }
              } else {
                  set.add(str);
                  hm.put(str, current);
                  current++;
              }
              sb = new StringBuilder();
          }
      }
      if (sb.toString() != ""){
        if (set.contains(sb.toString())) {
            if (hm.get(str) != null) {
                hm.remove(str);
            }
        } else {
            set.add(str);
            hm.put(str, current);
            current++;
        }
      }
      return hm.size() == 0 ? "" : hm.entrySet().iterator().next().getKey();
  }
}
