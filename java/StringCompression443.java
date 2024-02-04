import java.util.*;
public class StringCompression443 {

    public static int compress(char[] chars) {
        StringBuffer sc = new StringBuffer();
        int count = 0;
        sc.append(chars[0]);
        int j = 0;

        for (int i = 0; i < chars.length; i ++){
            if (chars[i] == sc.charAt(j)){
                count++;
                if (i == chars.length-1 && count != 1){
                    sc.append(count);
                }
            } else if (chars[i] != sc.charAt(j)) {
                if (count != 1){
                    sc.append(count);
                }

                sc.append(chars[i]);
                count = 1;
                j = sc.length()-1;

            }


        } for (int x = 0; x < sc.length(); x ++){
            chars[x] = sc.charAt(x);
        }

        return sc.length();
    }



    public static void main(String[] args) {

        char[] chars =  {'a','b','b','b','b','b','b','b','b','b','b','b','b'};

        System.out.println(compress(chars));
    }
}