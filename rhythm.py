"""Ordinary nearest-grid rhythm quantization and Gaussian timing evaluation."""
import math


def quantize(performance, seconds_per_tick=.1, offset=0.0, grid=3):
    score=[]
    for note in performance:
        start=max(0,min(12-grid,round((note['on']-offset)/seconds_per_tick/grid)*grid))
        end=max(start+grid,min(12,round((note['off']-offset)/seconds_per_tick/grid)*grid))
        score.append({'id':note['id'],'pitch':note['pitch'],'start':start,'end':end})
    return score


def timing_log_likelihood(performance, score, seconds_per_tick, offset):
    total=0.0
    for observed,event in zip(performance,score):
        for name,boundary in [('on','start'),('off','end')]:
            sigma=observed['sigma_'+name]
            mean=offset+seconds_per_tick*event[boundary]
            total-=.5*((observed[name]-mean)/sigma)**2+math.log(sigma*math.sqrt(2*math.pi))
    return total
