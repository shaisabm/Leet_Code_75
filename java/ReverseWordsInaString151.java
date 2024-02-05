import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

class ReverseWordsInaString151 {

    public static String reverseWords(String s) {
        String[] result = s.split(" ");

        List<String> st = new ArrayList<>();

        for (String str : result) {
            if (str != ""){
                st.add(str);
            }
        }
        st = st.reversed();
        String stringPipe = String.join(" ", st);
        return stringPipe;

    }
    public static void main(String[] args){
       String s = "  hello      world  ";
        System.out.println(reverseWords(s));


    }
}