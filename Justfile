set dotenv-load

get-puzzle year day:
    mkdir -p {{year}}/day_{{day}}
    curl -b "session=$AOC_SESSION_TOKEN" https://adventofcode.com/{{year}}/day/{{day}} -o {{year}}/day_{{day}}/task.html
    ./day-thing.py {{year}}/day_{{day}}/task.html > {{year}}/day_{{day}}/task.md
    rm {{year}}/day_{{day}}/task.html


get-data year day:
    mkdir -p {{year}}/day_{{day}}
    curl -b "session=$AOC_SESSION_TOKEN" https://adventofcode.com/{{year}}/day/{{day}}/input -o {{year}}/day_{{day}}/input.txt
