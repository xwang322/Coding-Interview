class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        List<Integer>[] temp = new List[numCourses];
        int[] answer = new int[numCourses];
        if (numCourses == 0) return new int[0];
        if (prerequisites == null || prerequisites.length == 0 || prerequisites[0].length == 0) {
            for (int i = 0; i < numCourses; i++) {
                answer[i] = i;
            }
            return answer;
        }
        int[] degree = new int[numCourses];
        for (int i = 0; i < numCourses; i++) {
            temp[i] = new ArrayList<>();
        }
        for (int i = 0; i < prerequisites.length; i++) {
            degree[prerequisites[i][0]]++;
            temp[prerequisites[i][1]].add(prerequisites[i][0]);
        }
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < numCourses; i++) {
            if (degree[i] == 0) {
                queue.offer(i);
            }
        }
        int total = 0;
        while (!queue.isEmpty()) {
            int current = queue.poll();
            answer[total++] = current;
            for (Integer ele : temp[current]) {
                degree[ele]--;
                if (degree[ele] == 0) {
                    queue.offer(ele);
                }
            }
        }
        return total == numCourses ? answer : new int[0];
    }
}
