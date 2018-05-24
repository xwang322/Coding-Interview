// 问了一下什么是singleton, 怎么实现singleton
package me.singleton;
public class Singleton{
    private static Singleton uniqueInstance = null;
    private Singleton() {};
    public static Singleton getInstance(){
        if (uniqueInstance == null) uniqueInstance = new Singleton();
        return uniqueInstance;
    }
    public static void main(String[] args) {
        Singleton my = Singleton.getInstance();
        Singleton your = Singleton.getInstance();
        if (my == your) System.out.println("My and Your instance is the same.");
    }
}
