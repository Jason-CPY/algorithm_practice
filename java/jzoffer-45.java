import java.util.Arrays;
public class Solution {
    public boolean isContinuous(int [] numbers) {
        if(numbers == null || numbers.length == 0)
            return false;
        Arrays.sort(numbers);
        int zero_num = 0;
        while(numbers[zero_num] == 0)
            zero_num++;
        for(int i = 0; i < numbers.length - 1; i++){
            if(numbers[i] != 0){
                if(numbers[i] == numbers[i + 1])
                    return false;
                zero_num = zero_num - (numbers[i+1] - numbers[i]) + 1;
                if(zero_num < 0)
                    return false;
            }
        }
        return true;
    }
}