// a condition variable example
#include <iostream>
#include <thread>
#include <mutex>
#include <condition_variable>
using namespace std;

mutex mtx;
condition_variable cv;
bool ready = false;
void newprint(int threadid)
{
    unique_lock<mutex> lk(mtx);
    while (!ready) cv.wait(lk);
    cout << "thread " << threadid << endl;
}

void go()
{
    unique_lock<mutex> lck(mtx);
    ready = true;
    cv.notify_all();
}

int main(int argc, char* argv[])
{
    thread threads[3];
    for (int i = 0; i < 3; i++)
    {
        threads[i] = thread(newprint, i);
    }
    cout << "Threads are ready to go!" << endl;
    go();
    for (auto &th:threads)
    {
        th.join();
    }
    return 0;
}
