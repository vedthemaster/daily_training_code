public class Array_comparison {
    public static void main(String[] args){
         int arr1[] = {1,2,4,5,8,7,9};
         int arr2[] = {3,5,78,4,9};
         int arr3[]= {};

         for (int i=0;i< arr1.length; i++){
             for (int j=0; j<arr2.length;j++){
                 if(arr1[i] == arr2[j]){
                     arr3[i] = arr1[i];
                 }
             }
         }
         for (int i=0;i<arr3.length;i++){
             System.out.println(arr3[i]);
         }
    }
    
}
