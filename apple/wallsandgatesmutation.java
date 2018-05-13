import java.util.*;
import java.io.*;
class Solution {
    public static void main(String[] args) {
        int[][] question = new int[][]{{2147483647,-1,0,2147483647},{2147483647,2147483647,2147483647,-1},{2147483647,-1,2147483647,-1},{0,-1,2147483647,2147483647}};
        int[][] answer = wallsAndGates(question);
        for (int i = 0; i < answer.length; i++) {
            for (int j = 0; j < answer[0].length; j++) {
                System.out.println(answer[i][j]);
            }
        }
    }

    public static int[][] wallsAndGates(int[][] rooms) {
        int[][] answer = new int[rooms.length][rooms[0].length];
        for (int i = 0; i < rooms.length; i++) {
            answer[i] = Arrays.copyOf(rooms[i], rooms[i].length);
        }
        boolean[][] visited = new boolean[rooms.length][rooms[0].length];
        if (rooms.length == 0 || rooms[0].length == 0) return answer;
        Queue<int[]> queue = new LinkedList<>();
        for (int i = 0; i < rooms.length; i++) {
            for (int j = 0; j < rooms[0].length; j++) {
                if (rooms[i][j] == 0) {
                    queue.offer(new int[]{i, j});
                }
            }
        }
        int step = 1;
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                int[] position = queue.poll();
                int row = position[0];
                int col = position[1];
                visited[row][col] = true;
                if (row > 0 && rooms[row-1][col] != -1 && !visited[row-1][col]) {
                    if (answer[row-1][col] == Integer.MAX_VALUE) answer[row-1][col] = step;
                    else answer[row-1][col] += step;
                    queue.offer(new int[]{row-1, col});
                }
                if (row < rooms.length-1 && rooms[row+1][col] != -1 && !visited[row+1][col]) {
                    if (answer[row+1][col] == Integer.MAX_VALUE) answer[row+1][col] = step;
                    else answer[row+1][col] += step;
                    queue.offer(new int[]{row+1, col});
                }
                if (col > 0 && rooms[row][col-1] != -1 && !visited[row][col-1]) {
                    if (answer[row][col-1] == Integer.MAX_VALUE) answer[row][col-1] = step;
                    else answer[row][col-1] += step;
                    queue.offer(new int[]{row, col-1});
                }
                if (col < rooms[0].length-1 && rooms[row][col+1] != -1 && !visited[row][col+1]) {
                    if (answer[row][col+1] == Integer.MAX_VALUE) answer[row][col+1] = step;
                    else answer[row][col+1] += step;
                    queue.offer(new int[]{row, col+1});
                }
            }
            step++;
        }
      return answer;
    }
}
