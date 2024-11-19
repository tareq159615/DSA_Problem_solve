// Brute Force Approach---------------------------------------------------------




//// Better Approach---------------------------------------------------------



// // Optimal Approach---------------------------------------------------------


// me --------------


class Solution {
public:
    void rotate(vector<int>& arr, int k) {
        int n = arr.size();
        k = k % n; // Handle cases where k > n
        vector<int> temp(k);

        // Store the last k elements in temp
        for (int i = 0; i < k; i++) {
            temp[i] = arr[n - k + i];
        }

        // Shift the rest of the array to the right
        for (int i = n - 1; i >= k; i--) {
            arr[i] = arr[i - k];
        }

        // Copy the temporary array's elements to the front
        for (int i = 0; i < k; i++) {
            arr[i] = temp[i];
        }
    }
};
