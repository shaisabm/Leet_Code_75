import java.util.Arrays;
import java.math.BigInteger;

class GreatestCommonDivisorofStrings1071 {

    public static String gcdOfStrings(String str1, String str2) {
        StringBuilder merge1 = new StringBuilder();
        StringBuilder merge2 = new StringBuilder();
        merge1.append(str1 + str2);
        merge2.append(str2 + str1);

        BigInteger str1Len = new BigInteger(Integer.toString(str1.length()));
        BigInteger str2Len = new BigInteger(Integer.toString(str2.length()));

        if (!merge1.toString().equals(merge2.toString())){
            return "";
        }
        BigInteger gcd = str1Len.gcd(str2Len);
        Integer GCD = gcd.intValue();
        StringBuilder ans = new StringBuilder();
        for (int i = 0; i < GCD; i++ ){
            ans.append(str1.charAt(i));
        }
        return ans.toString();
    }


    public static void main(String[] args){
        String str1 = "ABCABC";
        String str2 = "ABC";
        System.out.println(gcdOfStrings(str1,str2));
    }
}