public class Solution {
    public int Fibonacci(int n) {
        if(n == 0){
            return 0;
        }
        int x = 1,a = 0,b = 1;
        int i = 0;
        int j = 0;
        while(x < n){
            i = b;
            j = a + b;
            a = i;
            b = j;
            x += 1;
        }
        return b;
    }
}