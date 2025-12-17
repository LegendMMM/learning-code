#include <stdio.h>
#include <string.h>
int getaddr(char *givename, char n[][13], int t)
{
    for ( int i = 0; i < t; i++)
    {
        if (strcmp(givename, n[i]) == 0)
            return i;
    }
    return -1;

}

int main(void)
{
    int n, total, num, give;

    while(scanf("%d", &n) == 1)
    {
        char name[10][13] = {};
        int money[10] = {};
        char tempNameList[10][13] = {};
        total = 0;
        num = 0;

        for(int i = 0; i < n; i++)
            scanf("%s", name[i]);
        for (int t = 0; t < n; t++)
        {
            scanf("%s", tempNameList[0]);
            scanf("%d %d", &total, &num);
            if(num == 0)
                continue;
            for(int i =1; i < num + 1; i++)
                scanf("%s", tempNameList[i]);
            give = total/num;
            for(int i =1; i < num + 1; i++)
                money[getaddr(tempNameList[i], name, n)] += give;
            money[getaddr(tempNameList[0], name, n)] -= give*num;
        }
        for (int i = 0; i < n; i++) {
            printf("%s %d\n", name[i], money[i]);
        }
        printf("\n");
    }
    return 0;
}
