// O(n) space
class Solution {
    public int climbStairs(int n) {
        if (n <= 0) return 0;
        if (n == 1) return 1;
        int[] steps = new int[n];
        steps[0] = 1;
        steps[1] = 2;
        for (int i = 2; i < n; i++) {
            steps[i] = steps[i-1] + steps[i-2];
        }
        return steps[n-1];
    }
}

// O(1) space
class Solution {
    public int climbStairs(int n) {
        if (n==0 || n==1 || n==2) return n;
        int count1 = 1;
        int count2 = 2;
        for (int i = 2; i < n; i++) {
            int temp = count2;
            count2 = count1+temp;
            count1 = temp;
        }
        return count2;
    }
}
