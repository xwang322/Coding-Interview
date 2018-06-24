/*
Inversion Count for an array indicates – how far (or close) the array is from being sorted. 
If array is already sorted then inversion count is 0. If array is sorted in reverse order that inversion count is the maximum. 
Formally speaking, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j
The sequence 2, 4, 1, 3, 5 has three inversions (2, 1), (4, 1), (4, 3)
*/

// trival: O(n^2)
// optimization: make use of merge sort, cnt of inversion can be divided into three parts
public class Solution {
  
  public static void main(String[] args) {
    int[] arr =  {1, 20, 6, 4, 5};
    System.out.print(inversion(arr));
    
  }

  public static int inversion(int[] arr) {
    return merge(arr,new int[arr.length], 0, arr.length-1);
    
  }
  
  public static int merge(int[] arr,int[] tmp, int start, int end) {
    int mid = (start+end)/2;
    
    int cnt = 0;
    if(start < end) {
      cnt += merge(arr,tmp,start,mid);
      cnt += merge(arr,tmp,mid+1,end);
      
      cnt += mergeTwo(arr,tmp,start,mid+1,end);
    }
    return cnt;
  }
  
  public static int mergeTwo(int[] arr, int[] tmp, int start, int mid, int end) {
    int i = start;
    int j = mid;
    int k = start;
    int cnt = 0;
    while(i<mid && j <= end) {
      if(arr[i] > arr[j]) {
        tmp[k++] = arr[j++];
        cnt += mid - i;
      } else {
        tmp[k++] = arr[i++];
      }
    }
    
    while(i<mid) {
      tmp[k++] = arr[i++];
    }
    while(j<=end) {
      tmp[k++] = arr[j++];
    }
   for(k=start;k<=end;k++) {
      arr[k] = tmp[k];
    }
    
    return cnt; 
  }
  
}