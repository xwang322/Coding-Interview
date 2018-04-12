class Solution {
    private static String one = "qwertyuiopQWERTYUIOP";
    private static String two = "asdfghjklASDFGHJKL";
    private static String three = "zxcvbnmZXCVBNM";
        
    public String[] findWords(String[] words) {
        List<String> answer = new ArrayList<String>();
        for(String word : words){
            if(conditionfit(word)){
                answer.add(word);
            }
        }
        
        String[] answers = new String[answer.size()];
        return answer.toArray(answers);
    }
    
    private boolean conditionfit(String word){
        char c = word.charAt(0);
        String rowcheck = three;
        if(one.indexOf(c) >= 0){
            rowcheck = one;
        }else if(two.indexOf(c) >= 0){
            rowcheck = two;
        }
        
        for(int i = 1; i < word.length(); i++){
            char check = word.charAt(i);
            if(rowcheck.indexOf(check) < 0){
                return false;
            }
        }
        return true;
    }
}