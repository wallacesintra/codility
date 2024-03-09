fun solution(A: IntArray): Int {
    var positive_value = mutableSetOf<Int>()

    for (i in 0 until A.size){
        if (A[i] > 0){
            positive_value.add(A[i])
        }
    }

    var smallest_possible_value = 1

    while (positive_value.contains(smallest_possible_value)){
        smallest_possible_value++
    }

    return smallest_possible_value  
}