#include <iostream>
using namespace std;

int getMax(int array[], int size)
{
    int current = array[0];
    for (int i = 1; i < size; i++)
    {
        if (array[i] > current)
        {
            current = array[i];
        }
    }
    return current;
}

void digitSort(int array[], int size, int flag)
{
    int temp[size];
    int count[10] = {0};
    for (int i = 0; i < size; i++)
    {
        count[(array[i]/flag)%10]++;
    }
    for (int i = 1; i < 10; i++)
    {
        count[i] += count[i-1];
    }
    for (int i = size-1; i >= 0; i--)
    {
        temp[ count[ (array[i]/flag)%10 ] - 1] = array[i];
        count[ (array[i]/flag)%10 ]--;
    }
    for (int i = 0; i < size; i++)
    {
        array[i] = temp[i];
    }
}

void radixSort(int array[], int size)
{
    int m = getMax(array, size);
    for (int flag = 1; m/flag > 0; flag *= 10)
    {
        digitSort(array, size, flag);
    }
}

void printArray(int array[], int size)
{
    for (int i = 0; i < size; i++)
    {
        printf("%d ", array[i]);
    }
    printf("\n");
}

int main (int argc, char* argv[])
{
    int array[] = {5,1,8,3,2,9,7};
    int size = sizeof(array)/sizeof(array[0]);
    printf("Before the array is sorted:");
    printArray(array, size);
    radixSort(array, size);
    printf("After the array is sorted:");
    printArray(array, size);
    return 0;
}
