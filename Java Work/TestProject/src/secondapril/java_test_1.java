package secondapril;

import java.util.*;

public class java_test_1 {

    // public static void movezero(int arr[]){
    //     int c =0;
    //     for(int i:arr){
    //         if(i!=0){
    //             arr[c++]=i;
    //         }
    //     }
    //     for(int i=0;i<arr.length;i++){
    //         arr[i]=0;
    //     }
    // }
    // public static void main(String[] args) {
    //     Scanner sc = new Scanner(System.in);
    //     int arra[]= new int[10];

    //     for(int i=0;i<arra.length;i++){
    //         arra[i]=sc.nextInt();
    //     }
    //     movezero(arra);
    //     for(int k=0;k<arra.length;k++){
    //         System.out.print(arra[k] + " ");
    //     }
    // }
    static void pushZerosToEnd(int arr[], int n)
    {
        int count = 0;  // Count of non-zero elements
 
        // Traverse the array. If element encountered is
        // non-zero, then replace the element at index 'count'
        // with this element
        for (int i = 0; i < n; i++)
            if (arr[i] != 0)
                arr[count++] = arr[i]; // here count is
                                       // incremented
 
        // Now all non-zero elements have been shifted to
        // front and 'count' is set as index of first 0.
        // Make all elements 0 from count to end.
        while (count < n)
            arr[count++] = 0;
    }
 
    /*Driver function to check for above functions*/
    public static void main (String[] args)
    {
        Scanner sc= new Scanner(System.in);
        int arr[] = new int[5];
        int n = arr.length;
        for(int j=0;j<n;j++){
            arr[j]=sc.nextInt();
        }
        pushZerosToEnd(arr, n);
        System.out.println("Array after pushing zeros to the back: ");
        for (int i=0; i<n; i++)
            System.out.print(arr[i]+" ");
    }
    
}
