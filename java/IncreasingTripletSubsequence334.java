
class IncreasingTripletSubsequence334 {
    public static boolean increasingTriplet(int[] nums) {
        Double first = Double.POSITIVE_INFINITY;
        Double second = Double.POSITIVE_INFINITY;
        for (int n: nums){
            if (n <= first){
                first = (double) n;
            } else if ( n <= second) {
                second = (double) n;
            } else return true;
        } return false;

    }


    public static void main(String[] args){
        int[] nums = {20, 100, 10, 0, 0, 0, 0, 0, 12, 5, 12, 13};
        System.out.println(increasingTriplet(nums));

    }
}