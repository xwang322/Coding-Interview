
import java.io.*;
import java.util.*;
/*
output the number of consecutive subsequenences whose sum is divisible by k

 Let's say that it starts in L position and ends in R position. It is divisible by k if and only if pref[L - 1] == pref[R] (modulo k) because their differnce is zero modulo k(by definition of divisibility). So for each fixed modulo, we can pick any two prefixes with this prefix sum modulo k(and there are exactly count[i] * (count[i] - 1) / 2 ways to do it).
*/
// 


public class Solution {
  public static int dividedByK(int[] arr, int k) {
    int[] sum = new int[arr.length +1];
    sum[0] = 0;
    int[] count = new int[arr.length];
    count[0] =1;
    int res = 0;
    for(int i=1;i<=arr.length;i++) {
      sum[i] = (sum[i-1] + arr[i-1])%k;
      count[sum[i]] ++;
    }
    
    for(int i=0;i<count.length;i++) {
      System.out.print(count[i]+ " ");
    }
    for(int i=0; i < k ;i++){
      res+= (count[i] * (count[i]-1)/2);
    }
    return res;
  }
  
  public static void main(String[] args) {
    int[] arr = {1,2,1,2,1,2};
    int k = 2;
    System.out.println(dividedByK(arr,k));
  }
  
  
}

