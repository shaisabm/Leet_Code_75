class IsSubsequence392 {
    public static boolean isSubsequence(String s, String t) {
        int count = 0;
        int index = 0;

        if (s.isEmpty()) {
            return true;
        }
        for (int i = 0; i < t.length(); i++){
            if (s.charAt(index) == t.charAt(i)){
                count ++;
                index ++;
            } if (count == s.length()){
                return true;
            }

        } return false;



    }
    public static void main(String[] args){
        String s = "abc";
        String t = "ahbgdc";
        System.out.println(isSubsequence(s,t));

    }
}