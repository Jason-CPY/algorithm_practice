public class Solution {
    private int count;
    public int InversePairs(int [] array) {
        count = 0;
        if(array != null){
            mergeSort(array, 0, array.length - 1);
        }
        return count;
    }

    private void mergeSort(int[] a, int start, int end){
        if(start >= end)
            return;
        int mid = start + (end - start) / 2;
        mergeSort(a, start, mid);
        mergeSort(a, mid+1, end);
        merge(a,start,mid,end);
    }

    private void merge(int[] a, int start, int mid, int end){
        int[] temp = new int[end-start+1];
        int i = start, j = mid + 1, k = 0;
        while (i <= mid && j <= end) {
            if (a[i] <= a[j])
                temp[k++] = a[i++];
            else {
                temp[k++] = a[j++];
                count = (count + mid - i + 1) % 1000000007;
            }
        }

        while (i <= mid)
            temp[k++] = a[i++];
        while (j <= end)
            temp[k++] = a[j++];
        for(k=0;k<temp.length;k++){
            a[start+k] = temp[k];
        }
    }
}