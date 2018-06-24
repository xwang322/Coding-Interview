/*
aaaccccbbbbb - > 3a4c5b, not good, e.g 111aaa->313a, decode -> 313 of 'a'
aaaccccbbbbb - > CaDcEb 
*/
#include <iostream>
#include <string>
using namespace std;
class Solution {
public:
    string compression(string str) {
    	string res="";
    	if(str.empty())return res;
    	for(int i=0, j=0; i < str.length();)
    	{
    		while(str[i]==str[j])i++;
    		res+= convert(i-j-1)+ str[j];
    		j=i;
    	}
    	return res;
    }
    string convert(int n){
    	string res="";
    	if(n < 26)res='A'+ n;
    	else{
    		while(n>0){
    			char ch= (n==0)? 'J' : (n%10 + 'A');
    			res=ch + res;
    			n=n/10;
    		}
    	}
    	return res;
    }
};
int main(){
	Solution ss;
	string str="aaaccccbbbbb";
	cout << ss.compression(str) << endl;

	return 0;
}
