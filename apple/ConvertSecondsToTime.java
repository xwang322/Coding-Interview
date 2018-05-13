// 设计一个函数，输入n表示n秒，输出n秒的自然表示，例如3721就是1 hour 2 minutes 1 second
import java.util.*;
import java.io.*;
class Solution {
    public static void main(String[] args) {
        int n = 3721;
        System.out.println(ConvertTime(n));
        n = 1;
        System.out.println(ConvertTime(n));
        n = 3599;
        System.out.println(ConvertTime(n));
    }

    public static String ConvertTime(int n) {
        String answer = "";
        int hour = n/3600;
        n %= 3600;
        int minute = n/60;
        n %= 60;
        int second = n;
        StringBuilder sb = new StringBuilder();
        String hours;
        String minutes;
        String seconds;
        if (hour > 1) hours = new String("hours");
        else hours = new String("hour");
        if (minute > 1) minutes = new String("minutes");
        else minutes = new String("minute");
        if (hour > 1) seconds = new String("seconds");
        else seconds = new String("second");
        sb.append(Integer.toString(hour) + " " + hours + " " + Integer.toString(minute) + " " + minutes + " " + Integer.toString(second) + " " + seconds);
        return sb.toString();
    }
 }
