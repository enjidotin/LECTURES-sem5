#include <stdio.h>
#include <string.h>

char findClass(char str[])
{
    char arr[4];
    int i = 0;
    while (str[i] != '.')
    {
        arr[i] = str[i];
        i++;
    }
    i--;

    int ip = 0, j = 1;
    while (i >= 0)
    {
        ip = ip + (str[i] - '0') * j;
        j = j * 10;
        i--;
    }

    if (ip >= 1 && ip <= 126)
        return 'A';

    else if (ip >= 128 && ip <= 191)
        return 'B';

    else if (ip >= 192 && ip <= 223)
        return 'C';

    else if (ip >= 224 && ip <= 239)
        return 'D';

    else if (ip >= 240 && ip <= 254)
        return 'E';
    else
        printf("INVALID INPUT PLEASE RERUN");
}

void separate(char str[], char ip_CLASS)
{
    char network[12], host[12];
    for (int k = 0; k < 12; k++)
        network[k] = host[k] = '\0';

    if (ip_CLASS == 'A')
    {
        int i = 0, j = 0;
        while (str[j] != '.')
            network[i++] = str[j++];
        i = 0;
        j++;
        while (str[j] != '\0')
            host[i++] = str[j++];
        printf("Network ID is %s\n", network);
        printf("Host ID is %s\n", host);
    }

    else if (ip_CLASS == 'B')
    {
        int i = 0, j = 0, dotCount = 0;

        while (dotCount < 2)
        {
            network[i++] = str[j++];
            if (str[j] == '.')
                dotCount++;
        }
        i = 0;
        j++;

        while (str[j] != '\0')
            host[i++] = str[j++];

        printf("Network ID is %s\n", network);
        printf("Host ID is %s\n", host);
    }

    else if (ip_CLASS == 'C')
    {
        int i = 0, j = 0, dotCount = 0;

        while (dotCount < 3)
        {
            network[i++] = str[j++];
            if (str[j] == '.')
                dotCount++;
        }

        i = 0;
        j++;

        while (str[j] != '\0')
            host[i++] = str[j++];

        printf("Network ID: %s\n", network);
        printf("Host ID: %s\n", host);
    }

    else
        printf("In this Class, IP address is not"
               " divided into Network and Host ID\n");
}

int main()
{
    char str[] = "192.226.12.11";
    printf("Enter ip: ");
    scanf("%s", str);

    char ip_CLASS = findClass(str);
    printf("IP belongs to Class %c\n",
           ip_CLASS);
    separate(str, ip_CLASS);
    return 0;
}
