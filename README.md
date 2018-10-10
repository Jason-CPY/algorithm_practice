# algorithm_practice
剑指offer练习，顺便学习java

### 长记性：
1、java中的双引号和单引号作用不一样，不能像python一样乱用！  
2、```str.length()``` **VS** ```array.length```    
3、array必须要指定大小，不确定大小使用ArrayList  
```import java.util.Arrays;``` **VS** ```import java.util.ArrayList;```  
```int[] a = new int[10];``` **VS** ```ArrayList<Integer> a=new ArrayList<Integer>();```  
```System.out.println(Arrays.toString(a));``` **VS** ```System.out.println(a);```  
4、Java一行声明多个变量 **VS** Python一行声明多个变量  
```int x = 1,a = 0,b = 1;``` **VS** ```x,a,b = 1,0,1```  
5、Java Integer类型的Arraylist要转int类型的数组只能一个元素一个元素的```Integer.intValue()```,没有找到直接转的函数  
