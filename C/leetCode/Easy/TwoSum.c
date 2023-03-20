int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int *res;
    *returnSize = 2;

    res = (int*)malloc(2*(sizeof(int)));

    for (int i = 0; i < numsSize; i++) {
        for (int j = i + 1; j < numsSize; j++) {
            if (nums[i]+nums[j] == target) {
                res[0] = i;
                res[1] = j;
            }
        }
    }
    return res;
}

// Runtime: 18% | Memory: 65.62%