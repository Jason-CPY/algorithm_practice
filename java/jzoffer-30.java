public class Solution {
    public int FindGreatestSumOfSubArray(int[] array) {
        if(array == null){
            return 0;
        }
        int g = -10000000;
        int l = -10000000;
        for(int i = 0; i < array.length; i++){
            g = ((array[i] + g) > array[i]) ? (array[i] + g) : array[i];
            l = (g > l) ? g : l;
        }
        return l;
    }
}