// Merge Sort
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
void merge(int array[], int left, int middle, int right) {
    int n1 = middle-left+1;
    int n2 = right-middle;
    int Left[n1];
    int Right[n2];
    for (int i = 0; i < n1; i++) {
        Left[i] = array[left+i];
    }
    for (int i = 0; i < n2; i++) {
        Right[i] = array[i+middle+1];
    }
    int i = 0;
    int j = 0;
    int k = left;
    while (i < n1 && j < n2) {
        if (Left[i] <= Right[j]) {
            array[k] = Left[i];
            i++;
        } else {
            array[k] = Right[j];
            j++;
        }
        k++;
    }
    while (i < n1) {
        array[k++] = Left[i++];
    }
    while (j < n2) {
        array[k++] = Right[j++];
    }
}

void mergeSort(int array[], int left, int right) {
    if (left < right) {
        int middle = left + (right-left)/2;
        mergeSort(array, left, middle);
        mergeSort(array, middle+1, right);
        merge(array, left, middle, right);
    }
}

void PrintArray(int array[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");
}

int main(int argc, char* argv[]) {
    int array[] = {1,5,8,2,4,9,6};
    int array_size = sizeof(array)/sizeof(array[0]);
    printf("Given the array is \n");
    PrintArray(array, array_size);
    mergeSort(array, 0, array_size-1);
    printf("After the sorted array is \n");
    PrintArray(array, array_size);
    return 0;
}
