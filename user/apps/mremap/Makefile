ifeq ($(ARCH), x86_64)
export PREFIX=x86_64-linux-musl-
else ifeq ($(ARCH), riscv64)
export PREFIX=riscv64-linux-musl-
endif


export CC=$(PREFIX)gcc

all: mremap
	mv mremap $(DADK_CURRENT_BUILD_DIR)

mremap: main.c
	$(CC) -static -o mremap main.c

clean:
	rm mremap *.o