public class MergeStringsAlternately1768 {

    public static String mergeAlternately(String word1, String word2) {
        StringBuilder marged = new StringBuilder();
        int x = 0;
        int w1 = 0;
        int w2 = 0;
        char[] s1 = word1.toCharArray();
        char[] s2 = word2.toCharArray();

        while ( (x < s1.length ) || (x < s2.length)){
            if (w1 < s1.length){
                marged.append(s1[w1]);
                w1 ++;
            } if (w2 < s2.length){
                marged.append(s2[w2]);
                w2++;
            } x++;

        } return marged.toString();
    }

    public static void main(String[] args) {
        String word1 = "abc";
        String word2 = "pqr";
        System.out.println(mergeAlternately(word1,word2));

    }
}