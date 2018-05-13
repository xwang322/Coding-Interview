/*
Coding:
Given a list of strings: ['running, 0800, 1000', 'swimming,1000,1100', 'eating,1100,1200','running,1115,1330'...].
The meaning of the strings are 'activity, start time, end time'
prob1. Write a function to output all the unique activities in the list
prob2. Write a function to calculate the duration of each activity in minutes
prob3. Write a function to merge all the time intervals in the list that have overlaps, leave the non-overlapping intervals alone, and finally output all non-overlapping time intervals after merging those that overlap. O(N^2) solution not acceptable.
*/
import java.util.*;
import java.io.*;
class Solution {
    public static void main(String[] args) {
        String[] input = new String[]{"running, 0800, 0930", "swimming,1000,1130", "eating,1100,1200","running,1115,1330"};
        List<String> answer1 = Activities(input);
        for (String str : answer1) {
            System.out.println(str);
        }
        List<String> answer2 = ActivitiesTime(input);
        for (String str : answer2) {
            System.out.println(str);
        }
        List<int[]> answer3 = TimeInterval(input);
        for (int[] interval : answer3) {
            System.out.println(interval[0] + " " + interval[1]);
        }

    }

    public static List<String> Activities(String[] strings){
        List<String> answer = new ArrayList<>();
        for (String str :  strings) {
            String[] str_list = str.split(",");
            if (str_list.length != 3) break;
            String activity = new String(str_list[0]);
            if (!answer.contains(activity)) answer.add(activity);
        }
        return answer;
    }

    public static List<String> ActivitiesTime(String[] strings){
        List<String> answer = new ArrayList<>();
        Map<String, Integer> hm = new HashMap<>();
        for (String str :  strings) {
            String[] str_list = str.split(",");
            if (str_list.length != 3) break;
            String activity = new String(str_list[0]);
            int start = Integer.parseInt(str_list[1].trim());
            int end = Integer.parseInt(str_list[2].trim());
            int minutes = (end-start)/100 * 60 + (end-start)%100;
            if (!hm.containsKey(activity)) hm.put(activity, minutes);
            else hm.put(activity, hm.get(activity)+minutes);
        }
        for (String str : hm.keySet()) {
            StringBuilder sb = new StringBuilder();
            sb.append(str + " : " + Integer.toString(hm.get(str)));
            answer.add(sb.toString());
        }
        return answer;
    }

    public static List<int[]> TimeInterval(String[] strings) {
        List<int[]> intervals = new ArrayList<>();
        for (String str :  strings) {
            String[] str_list = str.split(",");
            if (str_list.length != 3) break;
            int start = Integer.parseInt(str_list[1].trim());
            int end = Integer.parseInt(str_list[2].trim());
            int[] interval = new int[]{start, end};
            intervals.add(interval);
        }
        intervals.sort((i1, i2) -> Integer.compare(i1[0], i2[0]));
        List<int[]> answer = new ArrayList<>();
        for (int[] interval : intervals) {
            if (answer.size() != 0 && answer.get(answer.size()-1)[1] >= interval[0]) {
                int start = answer.get(answer.size()-1)[0];
                int end = Math.max(answer.get(answer.size()-1)[1], interval[1]);
                answer.remove(answer.size()-1);
                answer.add(new int[]{start, end});
            } else {
                answer.add(interval);
            }
        }
        return answer;
    }
}
