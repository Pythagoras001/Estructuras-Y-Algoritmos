#include <bits/stdc++.h>
using namespace std;
const int N = 1e5 + 1;
vector<int> g[N];
int n, u, v;
double dfs(int u, int p)
{
    double k = 0, c = 0;
    for (int v : g[u])
        if (v != p)
            c++, k += dfs(v, u);
    return c ? k / c + 1 : 0;
}
int main()
{
    cin >> n;
    for (int i = 1; i < n; i++)
        cin >> u >> v, g[u].push_back(v), g[v].push_back(u);
    printf("%.8lf", dfs(1, 0));
}