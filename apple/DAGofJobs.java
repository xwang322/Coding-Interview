// 给一个DAG of jobs， 箭头A->B表示A要在B之前执行，求一个合法的执行sequence
import java.util.*;
import java.io.*;
class Job {
        int first;
        int later;
        Job() {first = 0; later = 0;}
        Job(int f, int l) {this.first = f; this.later = l;}
}
class Solution {
    public static void main(String[] args) {
        Job job1 = new Job(0, 1);
        Job job2 = new Job(1, 0);
        Job job3 = new Job(2, 3);
        List<Job> jobs = new ArrayList<>();
        jobs.add(job1);
        jobs.add(job2);
        jobs.add(job3);
        int[] answer = findOrder(jobs);
        for (Integer each : answer) {
            System.out.println(each);
        }
    }

    public static int[] findOrder(List<Job> jobs) {
        Set<Integer> jobset = new HashSet<>();
        for (Job job : jobs) {
            jobset.add(job.first);
            jobset.add(job.later);
        }
        int numJobs = jobset.size();
        List<List<Integer>> temp = new ArrayList<>(numJobs);
        int[] answer = new int[numJobs];
        if (numJobs == 0) return new int[0];
        if (jobs == null || jobs.size() == 0) {
            for (int i = 0; i < numJobs; i++) {
                answer[i] = i;
            }
            return answer;
        }
        for (int i = 0; i < numJobs; i++) {
            temp.add(new ArrayList<>());
        }
        int[] degree = new int[numJobs];
        for (int i = 0; i < jobs.size(); i++) {
            degree[jobs.get(i).later]++;
            temp.get(jobs.get(i).first).add(jobs.get(i).later);
        }
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < numJobs; i++) {
            if (degree[i] == 0) {
                queue.offer(i);
            }
        }
        int total = 0;
        while (!queue.isEmpty()) {
            int current = queue.poll();
            answer[total++] = current;
            for (Integer ele : temp.get(current)) {
                degree[ele]--;
                if (degree[ele] == 0) {
                    queue.offer(ele);
                }
            }
        }
        return total == numJobs ? answer : new int[0];
    }
 }
