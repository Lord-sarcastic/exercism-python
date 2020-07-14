def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    top = []
    for i in range(3):
        try:
            top.append(max(scores))
        except ValueError:
            break
        else:
            scores.remove(max(scores))
    return top
