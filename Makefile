CC = gcc
CFLAGS = -std=c11 -Wall -Wextra -g -O0
DAY01_BIN = build/day01/demo

.PHONY: all day01 run-day01 verify clean

all: day01

day01: $(DAY01_BIN)

$(DAY01_BIN): lessons/day01/main.c
	mkdir -p build/day01
	$(CC) $(CFLAGS) $< -o $@

run-day01: day01
	./$(DAY01_BIN)

verify: day01
	test "$$(./$(DAY01_BIN))" = "Speed error: 20"
	@printf 'Day01 build and output check passed.\n'

clean:
	rm -f $(DAY01_BIN)
