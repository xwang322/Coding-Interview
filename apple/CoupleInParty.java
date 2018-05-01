// party = [person1, person2, ...] couple = [(person1, person2), (person3, person4), ...]  找出 party 里所有的 couple where 夫妻两个人都在party里。
import java.util.*;
import java.io.*;
class Couple {
    String husband;
    String wife;
    Couple (String h, String w) {
        this.husband = h;
        this.wife = w;
    }
}

class Solution {
    public static void main(String[] args) {
        String[] party = {"Susan", "Dan", "Vernon", "Xiaodong", "Mengmeng", "Luke"};
        Couple p1 = new Couple("Xiaodong", "Mengmeng");
        Couple p2 = new Couple("Dan", "Sushi");
        Couple p3 = new Couple("Vernon", "Susan");
        List<Couple> couples = Arrays.asList(p1, p2, p3);
        List<Couple> answer = FindCouple(party, couples);
        for (Couple each : answer) {
            System.out.println(each.husband);
            System.out.println(each.wife);
        }
    }

    public static List<Couple> FindCouple(String[] party, List<Couple> couples) {
        if (party == null || party.length == 0 || couples == null || couples.size() == 0) return null;
        List<Couple> answer = new ArrayList<Couple>();
        Set<String> set = new HashSet<>();
        for (String person : party) {
            set.add(person);
        }
        for (int i = 0; i < couples.size(); i++) {
            if (set.contains(couples.get(i).husband) && set.contains(couples.get(i).wife)) answer.add(couples.get(i));
        }
        return answer;
    }
}
