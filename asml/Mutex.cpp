// a simple code for lock in cpp
#include <iostream>
#include <thread>
#include <mutex>
#include <chrono>
using namespace std;

int number = 0;
mutex lock_mutex;
void increment (int id)
{
    for (int i = 0; i < 3; i++)
    {
        lock_mutex.lock();
        number++;
        cout << id << " is " << number << "\n";
        lock_mutex.unlock();
        this_thread::sleep_for(chrono::seconds(1));
    }
}

int main(int argc, char* argv[])
{
    thread t1(increment, 0);
    thread t2(increment, 1);
    t1.join();
    t2.join();
    return 0;
}
