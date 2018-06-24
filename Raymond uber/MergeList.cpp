/*
merge two sorted lists
*/
#include <iostream>
#include <string>
#include <vector>
using namespace std;
struct ListNode
{
	int val;
	ListNode * next;
	ListNode(int x): val(x), next(NULL){};
	
};
class Solution {
public:
    ListNode * merge(ListNode * l1, ListNode * l2){
    	if(!l1)return l2;
    	if(!l2)return l1;

    	ListNode * head=NULL, *p=NULL;
    	if(l1->val < l2->val){
    		head=l1; l1=l1->next;
    	}
    	else{
    		head=l2;l2=l2->next;
    	}
    	p=head;
    	while(l1 && l2){
    		if(l1->val < l2->val){
    			p->next=l1;
    			l1=l1->next;
    		}
    		else {
    			p->next=l2;
    			l2=l2->next;
    		}
    		p=p->next;
    	}
    	if(l1)p->next=l1;
    	else p->next=l2;

    	return head;
    }
};
int main(){
	Solution ss;
	ListNode * l1=new ListNode(1);
	l1->next=new ListNode(3);
	l1->next->next=new ListNode(6);
	l1->next->next->next=new ListNode(7);

	ListNode * l2=new ListNode(1);
	l2->next=new ListNode(4);
	l2->next->next=new ListNode(5);
	l2->next->next->next=new ListNode(8);

	ListNode * head= ss.merge(l1, l2);
	while(head){
		cout << head->val << " ";//12345678
		head=head->next;
	}

	return 0;
}