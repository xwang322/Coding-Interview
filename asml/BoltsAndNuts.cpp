#include <iostream>
#include <queue>
#include <algorithm>
#include <vector>
#include <tuple>
using namespace std;
    vector<tuple<int, int>> BoltsAndNuts(vector<int>& bolts, vector<int>& nuts) {
        if (bolts.empty() || nuts.empty()) return {};
        vector<tuple<int, int>> answer;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq1;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq2;
        for (uint i = 0; i < bolts.size(); i++) {
            pq1.push(make_pair(bolts[i], i));
        }
        for (uint i = 0; i < nuts.size(); i++) {
            pq2.push(make_pair(nuts[i], i));
        }
        while (!pq1.empty() && !pq2.empty()) {
            auto val1 = pq1.top();
            pq1.pop();
            auto val2 = pq2.top();
            pq2.pop();
            if (val1.first == val2.first) {
                answer.push_back(make_tuple(val1.second, val2.second));
            }else if (val1.first > val2.first) {
                pq1.push(val1);
            }else {
                pq2.push(val2);
            }
        }
        return answer;
    }
int main(int argc, char* argv[]) {
  vector<int> b{3,5,6,8,12,14};
  vector<int> n{3,1,5,8,9,12};

  auto res = BoltsAndNuts(b,n);
  cout << "res is " << res.size() << endl;
  for(auto ele : res) {
    cout << get<0>(ele) << "  " << get<1>(ele) << endl;
  }
  return 0;
}
