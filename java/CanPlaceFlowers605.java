import java.math.*;

public class CanPlaceFlowers605 {
    public static boolean canPlaceFlowers(int[] flowerbed, int n) {
        if ((flowerbed.length == 1 && flowerbed[0] == 0 && (n == 1 || n == 0)) || (flowerbed.length == 1 && flowerbed[0] == 1 && n == 0)) {
            return true;
        } else if ((flowerbed.length == 1 && flowerbed[0] == 0 && n != 1) || (flowerbed.length == 1 && flowerbed[0] == 1 && n != 0) || (n > (flowerbed.length+1)/2)){
            return false;
        }
        int count = 0;
        for (int i = 0; i < flowerbed.length; i++){
            if (flowerbed[i] == 1){
                continue;
            } if (i == 0 && flowerbed[i+1] == 0){
                count++;
            } else if (i > 0 && i != flowerbed.length-1){
                if (flowerbed[i-1] == 0 && flowerbed[i+1] == 0){
                    count++;
                    flowerbed[i] = 1;
                }

            } else if (i == flowerbed.length-1 && flowerbed[i-1] == 0){
                count++;
            } if (count >= n){
                return true;
            }


        } return false;

    }
    public static void main(String[] args){


        int[] flowerbed = {0,0,0};
        int n = 2;
        System.out.println(canPlaceFlowers(flowerbed,n));
    }
}