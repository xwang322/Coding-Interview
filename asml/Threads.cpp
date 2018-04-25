// a simple program creating 3 threads and join
#include <iostream>
#include <thread>
using namespace std;

void foo(int z)
{
    for (int i = 0; i < z; i++)
    {
        cout << "Do something\n";
    }
}

class thread_obj{
public:
    void operator()(int x)
    {
        for(int i = 0; i < x; i++)
        {
            cout << "Not do something\n";
        }
    }
};

int main(int argc, char* argv[])
{
    cout << "Creating 3 threads now\n";
    thread th1(foo, 3);
    thread th2(thread_obj(), 2);
    auto f = [](int y) {
        for (int i = 0; i < y; i++)
        {
            cout << "Something interesting\n";
        }
    };
    thread th3(f, 4);
    th1.join();
    th2.join();
    th3.join();
    return 0;
}
