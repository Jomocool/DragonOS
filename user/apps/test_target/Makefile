CC=$(DragonOS_GCC)/x86_64-elf-gcc
LD=ld
OBJCOPY=objcopy

tmp_output_dir=$(ROOT_PATH)/bin/tmp/user
output_dir=$(DADK_BUILD_CACHE_DIR_TEST_TARGET_0_1_0)

all:
	mkdir -p $(tmp_output_dir)
	mkdir -p $(tmp_output_dir)/test_target
	RUSTFLAGS='-C target-feature=+crt-static -C link-arg=-no-pie' cargo +nightly-2023-08-15 -Z build-std=core,alloc,compiler_builtins install --target $(DADK_RUST_TARGET_FILE) --path .  --root $(tmp_output_dir)/test_target
	mv $(tmp_output_dir)/test_target/bin/test_target $(output_dir)/test_target
	rm -rf $(tmp_output_dir)/test_target
clean:
	cargo clean

fmt:
	cargo fmt