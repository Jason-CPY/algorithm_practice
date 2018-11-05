public class Solution {
    public int StrToInt(String str) {
        int n = str.length(), s = 1;
        int res = 0;
        if(n == 0) return 0;
        if(str.charAt(0) == '-') s = -1;
        for(int i = (str.charAt(0) ==  '-' || str.charAt(0) == '+') ? 1 : 0; i < n; ++i){
            if(!('0' <= str.charAt(i) && str.charAt(i) <= '9')) return 0;
            res=res*10+str.charAt(i)-'0';
        } 
        return res * s;
    }
}