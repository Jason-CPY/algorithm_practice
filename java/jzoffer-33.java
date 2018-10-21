import java.util.ArrayList;
public class Solution {
    public int GetUglyNumber_Solution(int index) {
        if(index < 1){
            return 0;
        }
        ArrayList<Integer> numList = new ArrayList<>();
        numList.add(1);
        int i2 = 0, i3 = 0, i5 = 0;
        int num = 0;
        int num2 = 0, num3 = 0, num5 = 0;
        while(numList.size() < index){
            num2 = numList.get(i2) * 2;
            num3 = numList.get(i3) * 3;
            num5 = numList.get(i5) * 5;
            num = Math.min(num2, num3) < num5 ? Math.min(num2, num3):num5;
            if(num == num2)
                i2 += 1;
            if(num == num3)
                i3 += 1;
            if(num == num5)
                i5 += 1;
            numList.add(num);
        }
        return numList.get(numList.size() - 1);
    }
}