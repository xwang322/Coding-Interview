class Solution {
    public void wallsAndGates(int[][] rooms) {
        if (rooms.length == 0 || rooms[0].length == 0) return;
        Queue<int[]> queue = new LinkedList<>();
        for (int i = 0; i < rooms.length; i++) {
            for (int j = 0; j < rooms[0].length; j++) {
                if (rooms[i][j] == 0) {
                    queue.offer(new int[]{i, j});
                }
            }
        }
        while (!queue.isEmpty()) {
            int[] position = queue.poll();
            int row = position[0];
            int col = position[1];
            if (row > 0 && rooms[row-1][col] == Integer.MAX_VALUE) {
                rooms[row-1][col] = rooms[row][col]+1;
                queue.offer(new int[]{row-1, col});
            }
            if (row < rooms.length-1 && rooms[row+1][col] == Integer.MAX_VALUE) {
                rooms[row+1][col] = rooms[row][col]+1;
                queue.offer(new int[]{row+1, col});
            }
            if (col > 0 && rooms[row][col-1] == Integer.MAX_VALUE) {
                rooms[row][col-1] = rooms[row][col]+1;
                queue.offer(new int[]{row, col-1});
            }
            if (col < rooms[0].length-1 && rooms[row][col+1] == Integer.MAX_VALUE) {
                rooms[row][col+1] = rooms[row][col]+1;
                queue.offer(new int[]{row, col+1});
            }
        }
    }
}
