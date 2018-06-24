/*
numsIsland 变体
一个2d grid，由0和1组成。从某一个1开始，计算由相邻的1构成的区域的面积。
从第2行第3列的那个1开始计算，最后结果应该是8。也就是左边那些互相连接起来的1构成的面积。
Follow up：接上题，将每一个grid看成边长为1的正方形，计算上述区域的周长。
BFS or DFS
*/
import java.io.*;
import java.util.*;

class Point {
  int x,y;
  public Point(int a, int b  ) {
    x = a;
    y = b;
  }
}
class Solution {
  
  int cnt;
  int cir;
  final int[][] dir = {{0,1},{1,0},{0,-1},{-1,0}};
  public void numIsland(int[][] grid, int row, int col) {
    Queue<Point> q = new LinkedList<>();
    q.offer(new Point(row,col));
    
    while(!q.isEmpty()) {
      Point p = q.poll();
      int x= p.x;
      int y = p.y;
      for(int i=0;i<4;i++) {
        //System.out.println(i);
        if(isValid(grid,x+dir[i][0],y+dir[i][1]) && grid[x+dir[i][0]][y+dir[i][1]] == 1) {
          
          cnt++;
          cir+=2;
          q.offer(new Point(x+dir[i][0],y+dir[i][1]));
          grid[x+dir[i][0]][y+dir[i][1]] = 0;
        }
      }
    }
    System.out.println(cnt + " " + cir);
  }
   
  public boolean isValid(int[][] grid, int x, int y) {
    if(x<0 || y <0 || x>=grid.length || y>= grid[0].length) {
      return false;
    }
    return true;
  }
  public static void main(String[] args) {
    int[][] grid = {{0,0,1,0,0}, 
                    {0,1,1,0,1},
                    {0,0,1,0,0}, 
                    {1,1,1,1,0}};
    Solution s = new Solution();
    s.numIsland(grid,1,2);
    //System.out.println("sad");
    
  }
}