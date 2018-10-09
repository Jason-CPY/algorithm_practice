public class Solution {
    public int RectCover(int target) {
        if(target == 0){
            return 0;
        }
        if(target == 1){
            return 1;
        }
        if(target == 2){
            return 2;
        }
        int x = 0,a = 0,b = 1;
        int i = 0;
        int j = 0;
        while(x < target){
            i = b;
            j = a + b;
            a = i;
            b = j;
            x += 1;
        }
        return b;
    }
}