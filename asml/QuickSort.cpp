#include <iostream>
using namespace std;
int partition (int array[], int low, int high) {
    int pivot = array[high];
    int i  = low - 1;
    for (int j = low; j <= high-1; j++) {
        if (array[j] <= pivot) {
            i++;
            swap(array[i], array[j]);
        }
    }
    swap(array[i+1], array[high]);
    return i+1;
}

void quickSort(int array[], int low, int high) {
    if (low < high) {
        int pivot = partition(array, low, high);
        quickSort(array, low, pivot-1);
        quickSort(array, pivot+1, high);
    }
}

void printArray(int array[], int size) {
    for (int i = 0; i < size; i++) {
        cout << array[i] << endl;
    }
    cout << "\n";
}

int main(int argc, char* argv[]) {
    int array[] = {6,3,2,9,7,1};
    int size = sizeof(array)/sizeof(array[0]);
    printArray(array, size);
    quickSort(array, 0, size-1);
    printArray(array, size);
    return 0;
}
