#define _GNU_SOURCE

#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>

#define OLD_SIZE 1024
#define NEW_SIZE 1024

int main()
{
    void *old_addr = NULL;
    void *new_addr = NULL;

    // 创建一个原始内存映射区域
    old_addr = mmap(NULL, OLD_SIZE, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    new_addr = mmap(NULL, OLD_SIZE, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    if (old_addr == MAP_FAILED)
    {
        perror("mmap");
        exit(EXIT_FAILURE);
    }

    printf("Old address: %p\n", old_addr);
    // 在旧内存区域写入数据
    strcpy(old_addr, "Hello, this is old memory to be copied!");
    // 读取并打印旧内存区域的内容
    printf("Old memory contents: %s\n", old_addr);

    // 重新映射并改变大小
    new_addr = mremap(old_addr, OLD_SIZE, NEW_SIZE, MREMAP_MAYMOVE|MREMAP_FIXED|MREMAP_DONTUNMAP,new_addr);
    if (new_addr == MAP_FAILED)
    {
        perror("mremap");
        exit(EXIT_FAILURE);
    }
    printf("New address: %p\n", new_addr);
    printf("New memory contents: %s\n", new_addr);

    // 在新内存区域写入数据
    strcpy(new_addr, "Hello, this is new memory!");
    printf("New memory contents: %s\n", new_addr);

    // 由于没有取消原映射，读取并打印旧内存区域的内容
    printf("Old memory contents: %s\n", old_addr);

    // 释放内存映射区域
    munmap(old_addr, OLD_SIZE);
    munmap(new_addr, NEW_SIZE);

    return 0;
}