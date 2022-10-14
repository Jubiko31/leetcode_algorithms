#include <stdio.h>
#include <math.h>

int board[30];   //Chess board
int count = 0;   //Total number of possible solutions

int placeQueens(int pos) {
    int row;
    // from 1st row to the current row check with all previous queens
    for (row = 1; row < pos; row++) {
        //check if queen exists in same column or diagonally and therefore return false(0)
        if ((board[row] == board[pos]) || (abs(board[row] - board[pos]) == abs(row - pos))) {
            return 0;
        }
    }
    //if it passed validation, it means no queen exists in same column and therefore return true(1)
    return 1;
}

//function to count total solution possibilities and draw solution chess board
void SolveNQueen(int number) {
    int row, j;
    count++;
    printf("\n\n Solution #%d: \n", count);
    for (row = 1; row <= number; row++) {
        for (j = 1; j <= number; j++) {
            if (board[row] == j) {
                printf("Q\t");
            } else {
                printf("-\t");
            }
        }
        printf("\n");
    }
}

void Queen(int number) {
    int k = 1;
    board[k] = 0;
    while (k != 0) {
        do {
            board[k]++;
        } while((board[k] <= number) && !placeQueens(k));

        if (board[k] <= number) {
            if (k == number) {
                SolveNQueen(number);
            } else {
                k++;
                board[k] = 0;
            }
        }
        else {
            k--;
        }
    }
}

int main() {
    int numberOfQueens;
    printf("Enter number of Queens: ");
    scanf("%d", &numberOfQueens);
    Queen(numberOfQueens);
    printf("\nTotal Possible Solutaions = %d", count);
}