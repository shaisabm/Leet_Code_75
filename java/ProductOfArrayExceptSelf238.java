import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ProductOfArrayExceptSelf238 {
    public static int[] productExceptSelf(int[] nums) {
        List<Integer> left = new ArrayList<>();
        left.add(1);
        List<Integer> right = Arrays.asList(new Integer[nums.length]);
        for (int k = 0; k < right.size(); k ++){
            right.set(k,0);
        }
        for (int i = 0; i < nums.length; i ++){
            left.add(nums[i]*left.get(i));
        }
        right.set(nums.length-1, 1);
        right.set(right.size()-2, nums[right.size()-1]);
        int count = nums.length-3;
        while (count != -1){
            right.set(count, right.get(count+1)*nums[count+1]);
            count --;

        }
        List<Integer> ans = new ArrayList<>();
        for (int j = 0; j < right.size(); j++){
            ans.add(right.get(j)*left.get(j) );

        } int[] example1 = ans.stream().mapToInt(i->i).toArray();
        return example1;

    }

    public static void main(String[] args){
        int[] nums = {3, 4, 6, 1, 2};

        System.out.println(productExceptSelf(nums));
    }
}