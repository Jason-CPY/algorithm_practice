import java.util.Map;
import java.util.Iterator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map.Entry;
import java.util.Collection;
//num1,num2分别为长度为1的数组。传出参数
//将num1[0],num2[0]设置为返回结果
public class Solution {
    public void FindNumsAppearOnce(int [] array,int num1[] , int num2[]) {
        HashMap map = new HashMap();
        for(int i = 0;i < array.length; i++){
            if(!map.containsKey(array[i]))
                map.put(array[i],1);
            else
                map.put(array[i],2);
        }
        int[] num = new int[10];
        int a = 0;
        Iterator iter = map.entrySet().iterator();
        while(iter.hasNext()) {
            Map.Entry entry = (Map.Entry)iter.next();
            if((int)entry.getValue() == 1){
                num[a] = (int)entry.getKey();
                a++;
            }
        }
        num1[0] = num[0];
        num2[0] = num[1];
    }
}