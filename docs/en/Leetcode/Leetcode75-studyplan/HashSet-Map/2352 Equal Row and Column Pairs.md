[2352. Equal Row and Column Pairs](https://leetcode.com/problems/equal-row-and-column-pairs/)

Solved

Medium

Topics

Companies

Hint

Given a **0-indexed** `n x n` integer matrix `grid`, _return the number of pairs_ `(ri, cj)` _such that row_ `ri` _and column_ `cj` _are equal_.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

**Example 1:**

![](https://assets.leetcode.com/uploads/2022/06/01/ex1.jpg)

**Input:** grid = [[3,2,1],[1,7,6],[2,7,7]]
**Output:** 1
**Explanation:** There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]

**Example 2:**

![](https://assets.leetcode.com/uploads/2022/06/01/ex2.jpg)

**Input:** grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
**Output:** 3
**Explanation:** There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]

**Constraints:**

- `n == grid.length == grid[i].length`
- `1 <= n <= 200`
- `1 <= grid[i][j] <= 105`

## hashing:

hash the rows, and try to match with the columns

```java
class Solution {
    public int equalPairs(int[][] grid) {
        int n = grid.length;
        int total = 0;
        Map<String, Integer> m = new HashMap<>();
        for (int[] a: grid) {
            StringBuilder builder = new StringBuilder();
            for (int b: a) {
                builder.append(String.valueOf(b));
                builder.append(";");
            }
            m.put(builder.toString(), m.getOrDefault(builder.toString(), 0) + 1);
        }
        for (int i = 0; i < n; i++) {
            StringBuilder builder = new StringBuilder();
            for (int j = 0; j < n; j++) {
                builder.append(String.valueOf(grid[j][i]));
                builder.append(";");
            }
            total += m.getOrDefault(builder.toString(), 0);
        }
        return total;
    }
}
```

or instead of make it a string, we use the normal hashing with a random number

```java
class Solution {    private int rowHash(int[] row){
        int hash=0;
        for(int n: row){
            hash = n + hash * 5;
        }
        return hash;
    }

    private int colHash(int[][] grid, int col){
        int hash=0;
        for(int i=0; i<grid.length; i++){
            hash = grid[i][col] + hash * 5;
        }
        return hash;
    }
    public int equalPairs(int[][] grid) {
        int count=0;
        int n = grid.length;

        Map<Integer, Integer> rowMap = new HashMap<>();
        for(int i=0; i<n; i++){
            Integer rowHash = rowHash(grid[i]);
            rowMap.put(rowHash, 1 + rowMap.getOrDefault(rowHash,0));
        }

        for(int i=0; i<n; i++){
            Integer colHash = colHash(grid, i);
            count += rowMap.getOrDefault(colHash,0);
        }

        return count;
    }
}
```

## matrix iter:

do iterations in the matrix

so actually we can store another matrix which is the transpose of the original matrix

the compare the rows/columns

```java
class Solution {
    public int equalPairs(int[][] grid) {
        int n = grid.length;
        int[][] trans = new int[n][n];
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                trans[i][j] = grid[j][i];
            }
        }
        int ans=0;
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                if(Arrays.equals(trans[j], grid[i]))
                    ans++;
            }
        }
        return ans;
    }
}
```

