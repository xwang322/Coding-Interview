//heapsort
#include <iostream>
using namespace std;

void printArray(int array[], int size) {
    for (int i = 0; i < size; i++) {
        cout << array[i] << endl;
    }
    cout << "\n";
}

void heapify(int array[], int size, int index) {
    int largest = index;
    int left = 2*index+1;
    int right = 2*index+2;
    if (left < size && array[left] > array[largest]) {
        largest = left;
    }
    if (right < size && array[right] > array[largest]) {
        largest = right;
    }
    if (largest != index) {
        swap(array[index], array[largest]);
        heapify(array, size, largest);
    }
}

void heapSort(int array[], int size) {
    for (int i = size/2-1; i >= 0; i--) {
        heapify(array, size, i);
    }
    for (int i = size-1; i >= 0; i--) {
        swap(array[0], array[i]);
        heapify(array, i, 0);
    }
}


int main(int argc, char* argv[]) {
    int array[] = {1,5,3,9,7,8};
    int array_size = sizeof(array)/sizeof(array[0]);
    printf("Given the array is \n");
    printArray(array, array_size);
    heapSort(array, array_size);
    printf("After the sorted array is \n");
    printArray(array, array_size);
    return 0;
}
