# 0x04. Sandpiles
## Details
 By: Alexandre Gautier, Software Engineer at Holberton School Weight: 1Ongoing second chance project - startedJan 9, 2023 12:00 AM, must end byJan 16, 2023 12:00 AM An auto review will be launched at the deadline#### In a nutshell…
* Auto QA review:          0.0/16 mandatory      
* Altogether:         0.0%* Mandatory: 0.0%
* Optional: no optional tasks

## Resources
Read or watch :
* [Sandpiles - Numberphile](https://intranet.hbtn.io/rltoken/UVY3WFjMmCRlLcr-B2Krug) 

## Requirements
### General
* Allowed editors:  ` vi ` ,  ` vim ` ,  ` emacs ` 
* All your files will be compiled on Ubuntu 14.04 LTS
* Your programs and functions will be compiled with  ` gcc 4.8.4 `  using the flags  ` -Wall `  ` -Werror `  ` -Wextra `  and  ` -pedantic ` 
* All your files should end with a new line
* Your code should use the  ` Betty `  style. It will be checked using [betty-style.pl](https://github.com/hs-hq/Betty/blob/master/betty-style.pl) 
 and [betty-doc.pl](https://github.com/hs-hq/Betty/blob/master/betty-doc.pl) 

* You are not allowed to use global variables
* No more than 5 functions per file
* In the following examples, the  ` main.c `  files are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own  ` main.c `  files at compilation. Our  ` main.c `  files might be different from the one shown in the examples
* The prototypes of all your functions should be included in your header file called  ` sandpiles.h ` 
* Don’t forget to push your header file
* All your header files should be include guarded
## Tasks
### 0. Sandpiles sum
          mandatory         Progress vs Score           Score: 0.00% (Checks completed: 0.00%)         Task Body Write a function that computes the sum of two sandpiles
* Prototype:  ` void sandpiles_sum(int grid1[3][3], int grid2[3][3]); ` 
* You can assume that both  ` grid1 `  and  ` grid2 `  are individually stable
* A sandpile is considered stable when none of its cells contains more than 3 grains
* When your function is done,  ` grid1 `  must be stable
*  ` grid1 `  must be printed before each toppling round, only if it is unstable (See example)
* You’re not allowed to allocate memory dynamically
** Pay close attention to the example output - there is a specific way you must perform these calculations **
```bash
alex@~/0x04-sandpiles$ cat 0-main.c 
#include <stdlib.h>
#include <stdio.h>

#include "sandpiles.h"

/**
 * print_grid_sum - Print 3x3 grids sum
 * @grid1: Left 3x3 grid
 * @grid2: Right 3x3 grid
 *
 */
static void print_grid_sum(int grid1[3][3], int grid2[3][3])
{
    int i, j;

    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 3; j++)
        {
            if (j)
                printf(" ");
            printf("%d", grid1[i][j]);
        }

        printf(" %c ", (i == 1 ? '+' : ' '));

        for (j = 0; j < 3; j++)
        {
            if (j)
                printf(" ");
            printf("%d", grid2[i][j]);
        }
        printf("\n");
    }
}

/**
 * print_grid - Print 3x3 grid
 * @grid: 3x3 grid
 *
 */
static void print_grid(int grid[3][3])
{
    int i, j;

    for (i = 0; i < 3; i++)
    {
        for (j = 0; j < 3; j++)
        {
            if (j)
                printf(" ");
            printf("%d", grid[i][j]);
        }
        printf("\n");
    }
}

/**
 * main - Entry point
 *
 * Return: EXIT_SUCCESS or EXIT_FAILURE
 */
int main(void)
{
    int grid1[3][3] = {
        {3, 3, 3},
        {3, 3, 3},
        {3, 3, 3}
    };
    int grid2[3][3] = {
        {1, 3, 1},
        {3, 3, 3},
        {1, 3, 1}
    };

    print_grid_sum(grid1, grid2);

    sandpiles_sum(grid1, grid2);

    printf("=\n");
    print_grid(grid1);

    return (EXIT_SUCCESS);
}
alex@~/0x04-sandpiles$ gcc -Wall -Wextra -Werror -pedantic 0-main.c 0-sandpiles.c -o 0-sandpiles
alex@~/0x04-sandpiles$ ./0-sandpiles 
3 3 3   1 3 1
3 3 3 + 3 3 3
3 3 3   1 3 1
=
4 6 4
6 6 6
4 6 4
=
2 5 2
5 6 5
2 5 2
=
4 2 4
2 6 2
4 2 4
=
0 5 0
5 2 5
0 5 0
=
2 1 2
1 6 1
2 1 2
=
2 2 2
2 2 2
2 2 2
alex@~/0x04-sandpiles$ cat 1-main.c
Same as 0-main.c except:
int grid1[3][3] = {
        {0, 0, 0},
        {0, 0, 0},
        {0, 0, 0}
    };
    int grid2[3][3] = {
        {3, 3, 3},
        {3, 3, 3},
        {3, 3, 3}
    };
alex@~/0x04-sandpiles$ gcc -Wall -Wextra -Werror -pedantic 1-main.c 0-sandpiles.c -o 0-sandpiles
alex@~/0x04-sandpiles$ ./0-sandpiles 
0 0 0   3 3 3
0 0 0 + 3 3 3
0 0 0   3 3 3
=
3 3 3
3 3 3
3 3 3
alex@~/0x04-sandpiles$

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holbertonschool-interview ` 
* Directory:  ` 0x04-sandpiles ` 
* File:  ` 0-sandpiles.c ` 
 Self-paced manual review  Panel footer - Controls 
