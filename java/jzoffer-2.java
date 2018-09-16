public class Solution {
    public String replaceSpace(StringBuffer str) {
    	if(str == null || str.length() <= 0){
            return str.toString();
        }
        int space = 0;
        for(int i=0;i<str.length();i++){
            if(str.charAt(i) == ' '){
                space += 1;
            }
        }
        if(space == 0){
            return str.toString();
        }
        int p1 = str.length() - 1;
        str.setLength(str.length()+space*2);
        int p2 = str.length() - 1;
        while(p1 >= 0 || p1 != p2){
            if(str.charAt(p1) == ' '){
                str.setCharAt(p2--,'0');
                str.setCharAt(p2--,'2');
                str.setCharAt(p2--,'%');
            }
            else{
                str.setCharAt(p2--,str.charAt(p1));
            }
            p1--;
        }
        return str.toString();
    }
}