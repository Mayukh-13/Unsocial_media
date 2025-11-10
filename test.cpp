// ॐ भूर् भुवः स्वः।
// तत् सवितुर्वरेण्यं।
// भर्गो देवस्य धीमहि।
// धियो यो नः प्रचोदयात् ॥
#include <bits/stdc++.h>
using namespace std;
#define int long long
#define endl '/n'
void print_vector(vector<int> &v)
{
    for (int i = 0; i < v.size(); i++)
        cout << v[i] << ' ';
    cout << endl;
}
void solve()
{
    int n;
    cin >> n;
    vector<int> v(n);
    for (int i = 0; i < n; i++)
        cin >> v[i];
}
signed main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    int t;
    cin >> t;
    while (t--)
        solve();
}