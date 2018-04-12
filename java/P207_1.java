class Solution {
    //dfs
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        if (prerequisites == null || numCourses == 0 || prerequisites.length == 0) {
            return true;
        }
        int[] visited = new int[numCourses];
        Map<Integer, List<Integer>> map = new HashMap<Integer, List<Integer>>();
        for (int[] prerequisite : prerequisites) {
            if (!map.containsKey(prerequisite[1])) {
                map.put(prerequisite[1], new LinkedList<Integer>());
            }
            map.get(prerequisite[1]).add(prerequisite[0]);
        }
        for (int i = 0; i < numCourses; i++) {
            if (!dfs(visited, map, i)) {
                return false;
            }
        }
        return true;
    }
    
    
    private boolean dfs(int[] visited, Map<Integer, List<Integer>> map, int index) {
        if (visited[index] == -1) {
            return false;
        }
        if (visited[index] == 1) {
            return true;
        }
        visited[index] = -1;
        if (map.containsKey(index)) {
            for (int value : map.get(index)) {
                if (!dfs(visited, map, value)) {
                    return false;
                }
            }
        }
        visited[index] = 1;
        return true;
    }
}