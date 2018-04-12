class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        if (numCourses <= 0) return false;
        Queue<Integer> queue = new LinkedList<Integer>();
        int[] degree = new int[numCourses];
        for (int i = 0; i < prerequisites.length; i++) {
            degree[prerequisites[i][0]]++;
        }
        for (int i = 0; i < numCourses; i++) {
            if (degree[i] == 0) {
                queue.offer(i);
            }
        }
        while(!queue.isEmpty()) {
            int x = queue.poll();
            for (int i = 0; i < prerequisites.length; i++) {
                if (x == prerequisites[i][1]) {
                    degree[prerequisites[i][0]]--;
                    if (degree[prerequisites[i][0]] == 0){
                        queue.offer(prerequisites[i][0]);
                    }
                }
            }
        }
        for (int i = 0; i < degree.length; i++) {
            if (degree[i] != 0) return false;
        }
        return true;
    }
}