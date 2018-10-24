public class Solution {
    public int GetNumberOfK(int [] array , int k) {
        double a = k;
       return search(array, a+0.5) - search(array, a-0.5);
    }
    
    public int search(int[] data, double n){
        int s = 0;
        int l = data.length - 1;
        int mid = 0;
        while(s <= l){
            mid = (s + l)/2;
            if(data[mid] < n)
                s = mid + 1;
            else
                l = mid - 1;
        }
        return s;
    }
}