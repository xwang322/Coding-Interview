class Solution {
    // dfs
    int length;
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        length = numCourses - 1;
        int[] result = new int[numCourses];
        int[] visited = new int[numCourses];
        Map<Integer, List<Integer>> map = new HashMap<Integer, List<Integer>>();
        for(int[] prerequisite: prerequisites) {
            if (!map.containsKey(prerequisite[1])) {
                map.put(prerequisite[1], new LinkedList<Integer>());
            }
            map.get(prerequisite[1]).add(prerequisite[0]);
        }
        for (int i = 0; i < numCourses; i++) {
            if (!dfs(map, visited, result, i)) {
                return new int[0];
            }            
        }
        return result;
    }
    
    private boolean dfs(Map<Integer, List<Integer>> map, int[] visited, int[] result, int index) {
        if (visited[index] == -1) {
            return false;
        }
        if (visited[index] == 1) {
            return true;
        }
        visited[index] = -1;
        if (map.containsKey(index)) {
            for (int value: map.get(index)) {
                if (!dfs(map, visited, result, value)) {
                    return false;
                }
            }
        }
        result[length--] = index;
        visited[index] = 1;
        return true;
    }
}