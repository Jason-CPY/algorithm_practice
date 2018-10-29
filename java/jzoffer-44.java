public class Solution {
    public String ReverseSentence(String str) {
        if(str.trim().equals("")) return str;
        String[] aa = str.split(" ");
        String res = "";
        int i = aa.length;
        for(;i > 0; i--){
            res += aa[i - 1];
            if(i > 1)
                res += " ";
        }
        return res;
    }
}