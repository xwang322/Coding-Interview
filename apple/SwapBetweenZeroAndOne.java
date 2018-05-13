/*
coding: 给一个只包含0和1的array：01100110 要求：相邻的数字不能相同。
所以有两种结果： 01010101和10101010，输出交换次数最少的交换过程 -> [[2,3],[6,7]]（01010101是交换次数最少的，输出的数字代表的是index，2和3交换，6和7交换）
*/
import java.util.*;
import java.io.*;
class Solution {
    public static void main(String[] args) {
        int[] nums = new int[]{0,0,0,0,0,1,1,1,1,1};
        List<List<Integer>> answer = SwapZeroAndOne(nums);
        for (List<Integer> each : answer) {
            System.out.println(each);
        }
    }

    public static List<List<Integer>> findMinimumSwap(int[] nums, int[] temp, List<List<Integer>> answer) {
        List<Integer> record = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            if (temp[i] != nums[i]) {
                record.add(i);
            }
        }
        while (!record.isEmpty()) {
            int j = -1;
            int k = -1;
            for (int i = 0; i < record.size(); i++) {
                int num = record.get(i);
                if (nums[num] == 0 && temp[num] == 1) j = num;
                else if (nums[num] == 1 && temp[num] == 0) k = num;
                if (j != -1 && k != -1) {
                    answer.add(new ArrayList<>(Arrays.asList(j, k)));
                    record.remove(new Integer(j));
                    record.remove(new Integer(k));
                    i -= 2;
                    j = -1;
                    k = -1;
                }
            }
        }
        return answer;
    }

    public static List<List<Integer>> SwapZeroAndOne(int[] nums) {
        List<List<Integer>> answer = new ArrayList<>();
        if (nums == null || nums.length == 0) return answer;
        //check if it returnable
        int[] counter = new int[2];
        for (Integer num : nums) {
            if (num == 0) counter[0]++;
            else if (num == 1) counter[1]++;
            else return answer;
        }
        if (Math.abs(counter[0] - counter[1]) > 1) return answer;
        if (Math.abs(counter[0] - counter[1]) == 1) {
            int[] temp = new int[nums.length];
            if (counter[0] > counter[1]) {
                for (int i = 0; i < nums.length; i++) {
                    temp[i] = i%2;
                }
            } else {
                for (int i = 0; i < nums.length; i++) {
                    temp[i] = (i+1)%2;
                }
            }
            answer = findMinimumSwap(nums, temp, answer);
            return answer;
        } else {
            int[] temp1 = new int[nums.length];
            int[] temp2 = new int[nums.length];
            for (int i = 0; i < nums.length; i++) {
                temp1[i] = i%2;
            }
            for (int i = 0; i < nums.length; i++) {
                temp2[i] = (i+1)%2;
            }
            List<List<Integer>> answer1 = new ArrayList<>();
            List<List<Integer>> answer2 = new ArrayList<>();
            answer1 = findMinimumSwap(nums, temp1, answer1);
            answer2 = findMinimumSwap(nums, temp1, answer2);
            if (answer1.size() > answer2.size()) return answer2;
            else return answer1;
        }
    }
 }
