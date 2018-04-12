class Solution {
    public List<String> readBinaryWatch(int num) {
        List<String> answer = new ArrayList<>();
        for (int t = 0; t < 12; t++) {
            for (int m = 0; m < 60; m++) {
                if (Integer.bitCount(t*64+m) == num) {
                   answer.add(String.format("%d:%02d", t, m)); 
                }
            }
        }
        return answer;
    }
}