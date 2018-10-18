import java.util.Arrays;
import java.util.ArrayList;
public class Solution {
    ArrayList<Integer> res = new ArrayList<>();
    public ArrayList<Integer> GetLeastNumbers_Solution(int [] input, int k) {
        if(input == null || k > input.length){
            return res;
        }
        Arrays.sort(input);
        for(int i = 0; i < k;i++){
            res.add(input[i]);
        }
        return res;
    }
}