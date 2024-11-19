#include <bits/stdc++.h>
using namespace std;

int main() {
    int arr[] = {13, 46, 24, 52, 20};
    int n = sizeof(arr) / sizeof(arr[0]);

    for (int i = 0; i < n - 1; i++) {  // n-1 because the last element will be sorted by then
        int min = i;
        for (int j = i + 1; j < n; j++) {  // Start from i+1
            if (arr[j] < arr[min]) min = j;
        }
        swap(arr[i], arr[min]);
    }

    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }

    return 0;
}
