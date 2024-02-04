import java.util.ArrayList;
import java.util.List;

class ReverseVowelsOfaString345 {

    public static String reverseVowels(String s) {
        List<Integer> index = new ArrayList<>();
        String vowels = "aeiouAEIOU";

        for(int i = 0; i < s.length(); i ++){
            if (vowels.contains(String.valueOf(s.charAt(i))) ){
                index.add(i);
            }
        }
        List<Integer> original = new ArrayList<>(index);
        index = index.reversed();

        int x = 0;
        char[] string = s.toCharArray();

        for (int j: original){
            string[j] = s.charAt(index.get(x));
            x++;
        }

        return String.valueOf(string);

    }
    public static void main(String[] args){
       String s = "leetcode";
        System.out.println(reverseVowels(s));

    }
}