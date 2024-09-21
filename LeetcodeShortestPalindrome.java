public class LeetcodeShortestPalindrome {
    public static  String shortestPalindrome(String s) {
        int base = 29;
        int power = 1;
        int last_index = 0;
        int size = s.length();
        int suffix = 0;
        int prefix = 0;
        if (size == 0) return "";
        for (int i = 0; i < size; i++) {
            int code = s.charAt(i) - 'a' + 1;   
            prefix = prefix * base + code;
            suffix = suffix + (code * power);
            power = power * base;
            if (prefix == suffix) {
                last_index = i;
            }
        }

        String suffixReversed = new StringBuilder(s.substring(last_index+1)).reverse().toString();
        return suffixReversed + s;
    }
}