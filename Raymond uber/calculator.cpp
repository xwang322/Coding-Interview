/*
１＋２*３/4, follow-up (1+2)*3 - 4*(5-8)
support all kinds of basic operation.
"100 * ( 2 + 12 )- (20 + 3)*2" = 1354
*/
#include <iostream>
#include <string>
#include <stack>
using namespace std;
class Solution {
public:
    bool level(char c1, char c2){
        if(c2=='(' || c2==')')return false;
        if((c1=='*' ||c1=='/') && (c2=='+'||c2=='-'))return false;
        else return true;
    }
    int calculate(char ch, int a, int b){
        if(ch=='+')return b+a;
        if(ch=='-')return b-a;
        if(ch=='*')return b*a;
        else return b/a;
    }
    int calculate(string s) {
        s.erase(remove(s.begin(), s.end(), ' '), s.end());
        if(s.length()==0)return 0;
        if(s.length()==1)return s[0]-'0';
        stack<int>val;
        stack<char>op;
        
        for(int i=0; i < s.length(); i++){
           
            if(s[i]<='9' && s[i] >='0'){
                string value="";
                while(i < s.length() && s[i] >='0' && s[i] <='9')value+=s[i++];
                val.push(stoi(value));
            }
            if(s[i]=='(')op.push('(');
            if(s[i]==')'){
                while(op.top()!='('){
                    int a=val.top();val.pop();
                    int b=val.top(); val.pop();
                    val.push(calculate(op.top(), a, b));
                    op.pop();
                }
                op.pop();
            }
            if(s[i]=='-' || s[i]=='+' ||s[i]=='*'||s[i]=='/'){
                
                while(!op.empty() && level(s[i], op.top())){
                    int a=val.top();
                    val.pop();
                    int b=val.top();
                    val.pop();
                    
                    val.push(calculate(op.top(), a, b));
                    op.pop();
                }
                
                op.push(s[i]);
            }
        }
        while(!op.empty()){
                int a=val.top();
                    val.pop();
                    int b=val.top();
                    val.pop();
                    val.push(calculate(op.top(), a, b));
                    op.pop();
            }
            return val.top();
        
    }
};
int main(){
	Solution ss;
	string expr="100 * ( 2 + 12 )- (20 + 3)*2";
	cout << ss.calculate(expr) << endl;
	return 0;
}