import java.util.HashMap;
public class Solution {
    public int FirstNotRepeatingChar(String str) {
        HashMap<Character,Integer> ha = new HashMap<>();
        for(int i=0; i<str.length(); i++){
            if(ha.get(str.charAt(i))==null){
                ha.put(str.charAt(i),1);
            }else{
                int tmp = ha.get(str.charAt(i));
                tmp++;
                ha.put(str.charAt(i),tmp);
            }
        }
        int index = -1;
        for(int i=0; i<str.length(); i++){
            if(ha.get(str.charAt(i))!=null && ha.get(str.charAt(i))==1){
                index = i;
                break;
            }
        }
        return index;
    }
}