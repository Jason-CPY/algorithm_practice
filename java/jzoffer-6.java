import java.util.ArrayList;
public class Solution {
    public int minNumberInRotateArray(int [] array) {
        if(array.length == 0){
            return 0;
        }
        if(array.length == 1){
            return array[0];
        }
        int l = array.length;
        int left = 0;
        int right = l - 1;
        int mid = 0;
        while(left <= right){
            mid = (left+right)/2;
            if(array[mid] > array[right]){
                left = mid + 1;
            }
            else if(array[mid] < array[right]){
                right = mid;
            }
            else{
                right -= 1;
            }
            if(left >= right){
                break;
            }
        }
        return array[left];
    }
}