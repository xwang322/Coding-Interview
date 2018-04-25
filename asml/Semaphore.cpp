// a small example about semaphore
#include <iostream>
#include <mutex>
#include <thread>
#include <condition_variable>
using namespace std;
mutex mtx;
condition_variable cv;
bool ready = false;
int current = 0;
void newprint(int num, int max)
{
    unique_lock<mutex> lock(mtx);
    while (num!= current || !ready) cv.wait(lock);
    current++;
    cout << "Current count is " << current << endl;
}

void go()
{
    unique_lock<mutex> lock(mtx);
    ready = true;
    cv.notify_all();
}

int main(int argc, char* argv[])
{
    int threadnumber = 5;
    thread threads[threadnumber];
    for (int i = 0; i < threadnumber; i++)
    {
        threads[i] = thread(newprint, i, threadnumber);
    }
    cout << "Running 5 threads in parallel\n";
    go();
    for (int i = 0; i < threadnumber; i++)
    {
        threads[i].join();
    }
    cout << "All threads are completed\n";
    return 0;
}
