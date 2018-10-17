import java.util.ArrayList;
import java.util.TreeSet;
public class Solution {
    public ArrayList<String> Permutation(String str) {
        ArrayList<String> res = new ArrayList<String>();
        if(str==null||str.length()==0){
            return res;
        }
        char[] charArray = str.toCharArray();
        TreeSet<String> tempRes = new TreeSet<String>();
        PermutationCore(charArray,tempRes,0);
        res.addAll(tempRes);
        return res;
    }
    
    private void PermutationCore( char[] charArray,TreeSet<String> tempRes,int loc){
        if(charArray==null || charArray.length==0 || loc<0 || loc>charArray.length-1){
            return ;
        }
        if(loc==charArray.length-1){
            tempRes.add(String.valueOf(charArray));//递归的出口
        }
        else{
            for(int i=loc;i<charArray.length;i++){
                swap(charArray,i,loc);//将第一个字符与后面的字符交换
                PermutationCore(charArray,tempRes,loc+1);//对后面所有的字符进行全排列
                swap(charArray,i,loc);//再将之前交换的字符交换回来，以便第一个字符再与其他字符交换
            }
        }
    }
    private void swap(char[] charArray,int i,int j){
        char temp = charArray[i];
        charArray[i] = charArray[j];
        charArray[j] = temp;
    }
}