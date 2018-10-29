import java.util.ArrayList;
public class Solution {
    public ArrayList<Integer> FindNumbersWithSum(int [] array,int sum) {
        int i = 0;
        int j = array.length - 1;
        ArrayList<Integer> res = new ArrayList<Integer>();
        while(i < j){
            if(array[i] + array[j] == sum){
                res.add(array[i]);
                res.add(array[j]);
                break;
            }
            while(i < j && array[i] + array[j] > sum)
                j--;
            while(i < j && array[i] + array[j] < sum)
                i++;
        }
        return res;
    }
}