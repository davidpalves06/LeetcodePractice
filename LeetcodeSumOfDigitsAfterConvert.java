
public class LeetcodeSumOfDigitsAfterConvert {
    public static int getLucky(String s, int k) {
        StringBuilder numericalRepresentation = new StringBuilder();
        for (char letter : s.toCharArray()) {
            numericalRepresentation.append(letter - 'a' + 1);
        }
        
        s = numericalRepresentation.toString();

        while (k > 0) {
            int digitSum = 0;
            for (char digit : s.toCharArray()) {
                digitSum += digit - '0';
            }
            if (digitSum < 10) {
                return digitSum;
            }
            k--;
            s = String.valueOf(digitSum);
        }
        return Integer.parseInt(s);
    }
}
