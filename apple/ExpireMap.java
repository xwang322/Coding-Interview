/*
expire map
实现一个ExpiringMap的两个操作，put操作和get操作，超时了取出来为null，没超时就能取出正确的value。
public void put(K key, V value, long durationMs) {}
public V get(K key) {}
ex:
// put(k, v, 1000)
// get(k) -> v (less than 1000 ms has passed since put)
// get(k) -> null (more than 1000 ms has passed since put)
*/
import java.util.*;
import java.io.*;
import java.sql.Timestamp;
class ExpireMap {
    Map<Integer, Integer> hm_value;
    Map<Integer, Long> hm_time;
    Long timestamp;
    public ExpireMap(){
        hm_value = new HashMap<>();
        hm_time = new HashMap<>();
    }
    public void put(int key, int value, long durations) {
        timestamp = new Long(System.currentTimeMillis());
        hm_value.put(key, value);
        hm_time.put(key, timestamp+durations);
    }
    public Integer get(int key) {
        timestamp = new Long(System.currentTimeMillis());
        if (!hm_value.containsKey(key)) return null;
        else {
            if (timestamp > hm_time.get(key)) return null;
            else return hm_value.get(key);
        }
    }
 }

 class Solution {
     public static void main(String[] args) {
         ExpireMap em = new ExpireMap();
         em.put(1, 2, 10);
         Long timestamp = new Long(System.currentTimeMillis());
         while (em.get(1) != null) {
             System.out.println(em.get(1));
         }
         System.out.println("Done");
     }
 }
