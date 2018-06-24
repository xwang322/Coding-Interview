
import java.io.*;
import java.util.*;
/*
设计一个EventListener要求实现register unregister 和 post 方法
*/
class Event {
  
  char id;
  public Event(char ID) {
    this.id = ID;
  }
  
  public void doEvent(String data) {
    System.out.println(id + data);
  }

  
  @Override
  public int hashCode() {
    return String.valueOf(id).hashCode();
  }
  
  @Override 
  public boolean equals(Object other) { //very important
    if(other instanceof Event) {
      return id == ((Event)other).id;
    }
    return false;
    
  }
}

class EventListener {
  Map<String,HashSet<Event>> map;
  
  public EventListener() {
    map = new HashMap<>();
  }
  
  public void register(String name , Event e) {
    if(!map.containsKey(name)) {
      map.put(name, new HashSet<Event>()); 
    }
    map.get(name).add(e);
  }
  
  public void unregister(String name, Event e) {
    if(!map.containsKey(name)) return;
    map.get(name).remove(e);
  }
  
  public void post(String name, String data) {
    if(!map.containsKey(name)) return;
    for(Event e : map.get(name)) {
      e.doEvent(data);
    }
  }
  
  
}



public class Solution {
  public static void main(String[] args) {
    EventListener Listener = new EventListener();
    Listener.register("div",new Event('A'));
    Listener.register("div", new Event('B'));
    //Listener.post("div", "hello");
    Listener.unregister("div", new Event('A'));
    Listener.post("div", "hello");
    Event e1 = new Event('A');
    Event e2 = new Event('A');
    System.out.println(e1.equals(e2));
    HashMap<Event,Integer> map = new HashMap<>();
    map.put(e1,2);
    System.out.println(e1.hashCode());
    System.out.println(e2.hashCode());
    System.out.println(e1.equals(e2));
  }
  
  
}

