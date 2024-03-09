fun solution(A : List<Int>): Int
{
    var max_gap = 0
    var gap = 0

    for (i in 0..A.size)
    {
        if (A[i] == 0)
        {
            gap++
        }
        else
        {
            if (gap > max_gap)
            {
                max_gap = gap
            }
            gap = 0
        }
    }
    return max_gap
}