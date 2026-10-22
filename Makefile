CC = gcc
CFLAGS = -std=c11 -Wall -Wextra -g -O0
CHAPTER1_BIN = build/CHAPT1/demo

.PHONY: all chapter1-c run-chapter1-c verify clean

all: chapter1-c

chapter1-c: $(CHAPTER1_BIN)

$(CHAPTER1_BIN): CHAPT1/main.c
	mkdir -p build/CHAPT1
	$(CC) $(CFLAGS) $< -o $@

run-chapter1-c: chapter1-c
	./$(CHAPTER1_BIN)

verify: chapter1-c
	test "$$(./$(CHAPTER1_BIN))" = "Speed error: 20"
	@printf 'Chapter 1 C build and output check passed.\n'

clean:
	rm -f $(CHAPTER1_BIN)
