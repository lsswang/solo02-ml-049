import json
from pathlib import Path
import rhythm
import fingering


def run(data):
    score=rhythm.quantize(data['performance'],data['seconds_per_tick'],data['offset'])
    return {'score':score,'timing_log_likelihood':rhythm.timing_log_likelihood(
        data['performance'],score,data['seconds_per_tick'],data['offset']),
        'fingering':fingering.plan(score,data['request'])}


if __name__=='__main__':
    data=json.loads((Path(__file__).parent/'fixtures/cases.json').read_text())
    print(json.dumps(run(data),indent=2))
