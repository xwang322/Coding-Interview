/*
一个2d grid，由0和1组成。从某一个1开始，计算由相邻的1构成的区域的面积。
从第2行第3列的那个1开始计算，最后结果应该是8。也就是左边那些互相连接起来的1构成的面积。
Follow up：接上题，将每一个grid看成边长为1的正方形，计算上述区域的周长。
BFS or DFS
*/
#include <iostream>
#include <vector>
#include <queue>
using namespace std;
typedef pair<int, int>mypair;
class Solution {
private:
	int count=1;
	int circumference=4;
public:
    int numIslands(vector<string>& grid, int i, int j) {
        int m=grid.size();
        if(m==0)return 0;

         helper(grid, i, j);
             
   
        return count;
    }
    int getircumference(){
    	return circumference;
    }
    
    void helper(vector<string>& grid, int i, int j){
        queue<mypair>q;
        q.push({i, j});
        grid[i][j]='0';
        int x, y;
        while(!q.empty()){
            x=q.front().first;
            y=q.front().second;
            q.pop();
            if(x > 0 && grid[x-1][y]=='1'){
            	count++;
            	circumference+=2;
                q.push({x-1,y}); grid[x-1][y]='0';
            }
            if(y > 0 && grid[x][y-1]=='1'){
            	count++;
            	circumference+=2;
                q.push({x,y-1}); grid[x][y-1]='0';
            }
            if(x < grid.size()-1 && grid[x+1][y]=='1'){
            	count++;
            	circumference+=2;
                q.push({x+1,y}); grid[x+1][y]='0';
            }
            if(y < grid[0].size()-1 && grid[x][y+1]=='1'){
            	count++;
            	circumference+=2;
                q.push({x,y+1}); grid[x][y+1]='0';
            }
        }
    }
};
int main(){
	Solution s;
	vector<string>grid={"00100", "01101","00100", "11110"};
	cout << s.numIslands(grid, 1, 2) << endl;
	cout << s.getircumference() << endl;

	return 0;
}