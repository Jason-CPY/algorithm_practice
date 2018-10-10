import java.util.ArrayList;
public class Solution {
    public void reOrderArray(int [] array) {
        if(array.length == 0 || array == null){
            return;
        }
        Integer[] arr = new Integer[array.length];
        ArrayList<Integer> a=new ArrayList<Integer>();
        ArrayList<Integer> b=new ArrayList<Integer>();
        for(int i = 0; i < array.length; i++){
            if(array[i] % 2 == 1){
                a.add(array[i]);
            }
            else{
                b.add(array[i]);
            }
        }
        a.addAll(b);
        a.toArray(arr);
        for(int j = 0; j < array.length; j++){
            array[j] = arr[j].intValue();
        }
    }
}