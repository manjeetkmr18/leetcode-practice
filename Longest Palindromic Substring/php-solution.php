class Solution {

/**
 * @param String $s
 * @return String
 */
function longestPalindrome($s) {
    
     $n = strlen($s);
    if ($n == 0) return "";
    
    $dp = array_fill(0, $n, array_fill(0, $n, false));
    $start = 0;
    $maxLength = 1;
    
    for ($i = 0; $i < $n; $i++) {
        $dp[$i][$i] = true;
    }
    
    for ($i = 0; $i < $n - 1; $i++) {
        if ($s[$i] == $s[$i + 1]) {
            $dp[$i][$i + 1] = true;
            $start = $i;
            $maxLength = 2;
        }
    }
    
    for ($len = 3; $len <= $n; $len++) {
        for ($i = 0; $i < $n - $len + 1; $i++) {
            $j = $i + $len - 1;
            if ($s[$i] == $s[$j] && $dp[$i + 1][$j - 1]) {
                $dp[$i][$j] = true;
                $start = $i;
                $maxLength = $len;
            }
        }
    }
    
    return substr($s, $start, $maxLength);

}
}