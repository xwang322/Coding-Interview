public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int a=n;
        int result=0;
        while(a!=0)
        {
            if((a&1)==1)
                result++;
            a>>>=1;
        }
        return result;
    }
}