// https://www.geeksforgeeks.org/problems/quick-sort/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=quick-sort
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    // Function to sort an array using quick sort algorithm.
    void quickSort(int arr[], int low, int high) {
        if (low < high) {
            int p = partition(arr, low, high); // Partition the array
            quickSort(arr, low, p - 1);       // Sort left partition
            quickSort(arr, p + 1, high);      // Sort right partition
        }
    }

    // Function to partition the array around the pivot
    int partition(int arr[], int low, int high) {
        int pivot = arr[low]; // Choose the first element as the pivot
        int i = low;
        int j = high;

        while (i < j) {
            while (arr[i] <= pivot && i < high) {
                i++;
            }
            while (arr[j] > pivot && j > low) {
                j--;
            }
            if (i < j) {
                swap(arr[i], arr[j]);
            }
        }
        swap(arr[j], arr[low]); // Place pivot in the correct position
        return j;
    }
};

int main() {
    int arr[] = {4, 6, 2, 5, 7, 9, 1, 3}; // Using a raw array
    int n = sizeof(arr) / sizeof(arr[0]); // Calculate the size of the array

    cout << "Before QuickSort:" << endl;
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    Solution sol;
    sol.quickSort(arr, 0, n - 1); // Call quicksort on the array

    cout << "After QuickSort:" << endl;
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

    return 0;
}
