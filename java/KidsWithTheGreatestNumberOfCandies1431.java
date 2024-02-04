import java.lang.annotation.Retention;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

public class KidsWithTheGreatestNumberOfCandies1431 {

    public static List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int max_candies = Arrays.stream(candies).max().getAsInt();
        List<Boolean> boolen = new ArrayList<>();
        System.out.println(max_candies);
        for (int i = 0; i < candies.length; i ++) {
            if (candies[i] + extraCandies >= max_candies) {
                boolen.add(Boolean.TRUE);
            } else boolen.add(Boolean.FALSE);
        } return boolen;


    }


    public static void main(String[] args) {
        int[] candies = {2, 3, 5, 1, 3};
        int extraCandies = 3;
        kidsWithCandies(candies,extraCandies);
    }
}
