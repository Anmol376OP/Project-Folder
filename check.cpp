#include <bits/stdc++.h>
using namespace std;

int dfs(vector<int> &arr, vector<int> &visited, vector<int> &memo, int current)
{
    if (current == -1)
    {
        return INT_MIN;
    }
    if (visited[current] == 1)
    {
        return memo[current];
    }

    visited[current] = 1;
    int next = arr[current];
    int cycleSum = dfs(arr, visited, memo, next) + 1;

    visited[current] = 0;

    memo[current] = cycleSum;
    return cycleSum;
}

int findLargestCycleSum(vector<int> &arr)
{
    int n = arr.size();
    vector<int> memo(n + 1, 0);
    vector<int> visited(n + 1, 0);
    int maxCycleSum = 0;
    for (int i = 0; i < n; i++)
    {
        if (visited[i] == 0)
        {
            int cycleSum = dfs(arr, visited, memo, i);
            maxCycleSum = max(maxCycleSum, cycleSum);
        }
    }
    return maxCycleSum;
}
int main()
{
    vector<int> arr = {4, 4, 1, 4, 13, 8, 8, 8, 0, 8, 14, 9, 15, 11, -1, 10, 15, 22, 22, 22, 22, 22, 21};
    int largestCycleSum = findLargestCycleSum(arr);
    cout << "Largest Sum Cycle: " << largestCycleSum << endl;
    return 0;
}