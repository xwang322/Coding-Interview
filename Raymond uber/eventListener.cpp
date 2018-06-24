/*
设计一个EventListener要求实现register unregister 和 post 方法
*/
#include <iostream>
#include <vector>
#include <unordered_set>
#include <unordered_map>
using namespace std;

/*class Event{
private:
	string Data;
public:
	char ID;
	Event(char id){
		ID=id;
	}
	void doEvent(string data){
		Data=data;
		switch(ID){
			case 'A': cout << Data << " functionA " << endl;
					   break;
			case 'B': cout << Data << " functionB " << endl;
				       break;
			default: cout << "none" << endl;
				 	  break;
		}

	}
};

inline bool operator == (Event const a, Event const b){return a.ID==b.ID;}
class EventListener {
struct hash{
	size_t operator() (const Event e) const{
		int id=e.ID-'0';
		return id;
	}
};
private:
	unordered_map< string, unordered_set<Event, hash > >table;
public:

};
int main()
{
	
	EventListener Listener;
	//Listener.register("first", Event('A'));
	

	return 0;
}*/
class Event{
public:
	char ID;
	Event(char id){
		ID=id;
	}
	void doEvent(string data) const{
		switch (ID){
			case'A': cout << data << " with functionA" << endl;
					break;
			case'B': cout << data << " with functionB" << endl;
					break;
			default: cout << "none" << endl;
					break;
		}
	}

};
inline bool operator == (Event const & a, Event const & b){return a.ID==b.ID;}
class EventListener {
struct hash{
	size_t operator() (Event const & e)const {
		int id=e.ID-'0';
		return id;
	}
};
private:
	unordered_map< string, unordered_set<Event, hash > >table;
public:
	void Register(string name, Event e){
		if(!table.count(name))table[name]={e};
		else table[name].insert(e);
	}
	void Unregister(string name, Event e){
		if(!table.count(name))return;
		table[name].erase(e);
	}
	void post(string name, string data){
		if(!table.count(name))return;
		for(auto iter=table[name].begin(); iter!=table[name].end(); iter++){
			iter->doEvent(data);
		}
	}
};
int main()
{
	
	EventListener Listener;
	Listener.Register("div", Event('A'));
	Listener.Register("div", Event('B'));
	Listener.post("div", "hello");
	

	return 0;
}