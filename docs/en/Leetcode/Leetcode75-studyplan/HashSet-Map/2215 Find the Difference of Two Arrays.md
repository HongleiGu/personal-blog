[2215. Find the Difference of Two Arrays](https://leetcode.com/problems/find-the-difference-of-two-arrays/)

Given two **0-indexed** integer arrays `nums1` and `nums2`, return _a list_ `answer` _of size_ `2` _where:_

- `answer[0]` _is a list of all **distinct** integers in_ `nums1` _which are **not** present in_ `nums2`_._
- `answer[1]` _is a list of all **distinct** integers in_ `nums2` _which are **not** present in_ `nums1`.

**Note** that the integers in the lists may be returned in **any** order.

**Example 1:**

**Input:** nums1 = [1,2,3], nums2 = [2,4,6]
**Output:** `[[1,3],[4,6]]`
**Explanation:**
For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6].

**Example 2:**

**Input:** nums1 = [1,2,3,3], nums2 = [1,1,2,2]
**Output:** `[[3],[]]`
**Explanation:**
For nums1, nums1[2] and nums1[3] are not present in nums2. Since nums1[2] == nums1[3], their value is only included once and answer[0] = [3].
Every integer in nums2 is present in nums1. Therefore, answer[1] = [].

**Constraints:**

- `1 <= nums1.length, nums2.length <= 1000`
- `-1000 <= nums1[i], nums2[i] <= 1000`

create two sets, and then iteratively add all the elements and then check the difference

```java
class Solution {

    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {

        Set<Integer> s1 = new HashSet<Integer>();

        Set<Integer> s2 = new HashSet<Integer>();

        List<Integer> l1 = new ArrayList<Integer>();

        List<Integer> l2 = new ArrayList<Integer>();

        for (int i: nums1) {

            s1.add(i);

        }

        for (int i: nums2) {

            s2.add(i);

        }

        for (int i: s1) {

            if (!s2.contains(i)) {

                l1.add(i);

            }

        }

        for (int i: s2) {

            if (!s1.contains(i)) {

                l2.add(i);

            }

        }

        return new ArrayList<List<Integer>>() {{

            add(l1);

            add(l2);

        }};

    }

}
```

or we could make it syntactically simpler with the internal functions
```java
class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        

        Set<Integer> set1 = new HashSet<>();
        Set<Integer> set2 = new HashSet<>();

        for(int num : nums1)
        {
            set1.add(num);
        }
        for(int num : nums2)
        {
            set2.add(num);
        }

        List<Integer> up1 = new ArrayList<>(set1);
        List<Integer> up2 = new ArrayList<>(set2);

        up1.removeAll(set2);

        up2.removeAll(set1);

      List<List<Integer>> result = new ArrayList<>();

        result.add(up1);
        result.add(up2);

        return result;
    }
}
```