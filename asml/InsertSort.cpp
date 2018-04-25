#include <iostream>
using namespace std;

void quickSort(int array[], int size)
{
    int i, j, key;
    for (i = 1; i < size; i++)
    {
        key = array[i];
        j = i-1;
        while (j >= 0 && array[j] > key)
        {
            array[j+1] = array[j];
            j--;
        }
        array[j+1] = key;
    }
}

void printArray(int array[], int size)
{
    for (int i = 0; i < size; i++)
    {
        printf("%d, ", array[i]);
    }
    printf("\n");
}

int main(int argc, char* argv[])
{
    int array[] = {8,4,2,9,5,1};
    int size = sizeof(array)/sizeof(array[0]);
    printf("Before the array is sorted: ");
    printArray(array, size);
    quickSort(array, size);
    printf("After the array is sorted: ");
    printArray(array, size);
    return 0;
}
