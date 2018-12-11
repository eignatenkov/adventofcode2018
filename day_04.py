from datetime import datetime, timedelta
import pandas as pd


def parse_line(line):
    date_string, instruction = line.split('] ')
    dt = datetime.strptime(date_string, "[%Y-%m-%d %H:%M")
    if dt.hour != 0:
        dt = dt.replace(hour=0, minute=0)
        dt += timedelta(days=1)
    if instruction.startswith('Guard'):
        instruction = int(instruction.split()[1].strip(' #'))
    else:
        instruction = instruction.strip()
    return dt, instruction


def read_input(filename):
    result_df = pd.DataFrame(columns=['mmdd', 'guard_id'] + list(map(str, range(60)))).set_index('mmdd')
    instructions = []
    with open(filename) as f:
        for line in f:
            dt, instruction = parse_line(line)
            if isinstance(instruction, int):
                result_df.loc[dt.strftime("%m%d"), 'guard_id'] = instruction
            else:
                instructions.append((dt, instruction))
    result_df.iloc[:, 1:] = 0
    instructions = sorted(instructions, key=lambda x: x[0])
    for dt, instruction in instructions:
        index = dt.strftime("%m%d")
        minute = dt.minute
        result_df.loc[index, str(minute):] = 1 if instruction == "falls asleep" else 0
    return result_df


if __name__ == "__main__":
    byminute_df = read_input("/home/egor/private/adventofcode2018/data/day04_input.txt")
    best_guard = (byminute_df.groupby('guard_id').sum().sum(axis=1).sort_values(ascending=False)).index[0]
    best_minute = (byminute_df[byminute_df.guard_id == best_guard].iloc[:, 1:].sum().sort_values(
        ascending=False)).index[0]
    print(best_guard * int(best_minute))
    sleepy_guard_df = byminute_df.groupby('guard_id').sum()
    sleepy_guard = sleepy_guard_df.max(axis=1).idxmax()
    sleepy_minute = sleepy_guard_df.loc[sleepy_guard].idxmax()
    print(sleepy_guard * int(sleepy_minute))