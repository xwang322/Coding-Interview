import java.io.*;
import java.util.*;

/*
 * To execute Java, please define "static void main" on a class
 * named Solution.
 *
 * If you need more classes, simply define them inline.
 */


/* 输入一组数据，用户名字，登录时间，登出时间，输出用户个数在所有登录/登出时间
['A', 1.1, 2.3],
['B', 1.3, 3.4]
output: 
[1.1, 1],
[1.3, 2],
[2.3, 1],
[3.4, 0]
*/
class Data {
  String name;
  double in;
  double out;
  public Data(String n, double i ,double o) {
    name = n;
    in = i;
    out = o;
  }
}

class Pair {
  int cnt;
  double time;
  public Pair(int c, double t) {
    cnt = c;
    time = t;
  }
  
  public String toString() {
    return String.valueOf(time) + " " + String.valueOf(cnt);
  }
}
class Solution {
  public static List<Pair>  logSystem(Data[] data) {
    List<Pair> ret = new ArrayList<Pair>();
    int len = data.length;
    double[] start = new double[len];
    double[] end = new double[len];
    for(int i=0;i<len;i++) {
      start[i] = data[i].in;
      end[i] = data[i].out;
      
    }
    Arrays.sort(start);
    Arrays.sort(end);
    int eidx = 0;
    int cnt = 0;
    for(int i=0;i<start.length;i++) {
      if(start[i] < end[eidx]) {
        cnt++;
        if(i==len-1 || start[i+1]!= start[i]) {
          ret.add(new Pair(cnt,start[i]));
        }
      } else {
        cnt--;
        if(eidx == len-1 || end[eidx+1]!= end[eidx]) {
          ret.add(new Pair(cnt,end[eidx]));
        }
        eidx++;
        i--;
      }
      while(i == start.length -1 && eidx < len) {
        cnt--;
        if(eidx == len-1 || end[eidx+1]!= end[eidx]) {
          ret.add(new Pair(cnt,end[eidx]));
        }
        eidx++;
      } 
    
    }
    
    return ret;
  }
  
  
  
  
  public static void main(String[] args) {
    //int[] arr = {1, 0, -1, 0, -2, 2};
    //sum(arr);
    Data[] data = { new Data("A", 1.1, 1.2), new Data("B", 1.3, 3.4),new Data("C", 1.1, 2.2), new Data("D", 1.1, 2.2)};
    for(Pair each : logSystem(data)) {
      System.out.println(each);
    }
  }
}