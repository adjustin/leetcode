
class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        HashMap<Integer, Integer> map1 = new HashMap<>();
        LinkedList<Integer> list = new LinkedList<>();
        for(int num: nums1){
            map1.put(num, map1.getOrDefault(num, 0) + 1);
        }
        for(int num: nums2){
            if(map1.containsKey(num) && map1.get(num) > 0){
                list.add(num);
                map1.put(num, map1.getOrDefault(num, 0) - 1);
            }
        }
        int[] ans = new int[list.size()];
        int i = 0;
        for(int num: list){
            ans[i++] = num;
        }
        return ans;
    }
}