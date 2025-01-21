from cal import RoundProcess
from file import read_round_data, write_results
from ppt import PPT

def main(round_number):
    round_data = read_round_data(f'../data/round{round_number}.txt')
    processor = RoundProcess(round_data, round_number)
    results = processor.process_round()
    write_results(f'../results/result{round_number}.txt', results)

    ppt = PPT(f"ppt{round_number}")
    for team_result in results:
        ppt.add_results(team_result)
    ppt.save()

if __name__ == "__main__":
    round_number = int(input())
    main(round_number)

