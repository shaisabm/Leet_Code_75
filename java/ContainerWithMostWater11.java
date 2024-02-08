import java.math.*;
class ContainerWithMostWater11 {

    public static int maxArea(int[] height) {
        int lastIndex = height.length-1;
        int maxArea = -1;
        int firstIndex = 0;

          while (firstIndex < lastIndex){
              int currentArea = (lastIndex - firstIndex)*Math.min(height[lastIndex],height[firstIndex]);

              if (maxArea < currentArea){
                  maxArea = currentArea;
              } if (height[firstIndex] < height[lastIndex]){
                  firstIndex ++;
              } else lastIndex --;
          } return maxArea;



    }
    public static void main(String[] args){
        int[] height = {1, 8, 6, 2, 5, 4, 8, 3, 7};
        System.out.println(maxArea(height));

    }
}