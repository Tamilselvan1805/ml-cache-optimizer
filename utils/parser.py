def load_requests(file_path, max_lines=10000):
    requests = []

    with open(file_path, "r") as f:
        for i, line in enumerate(f):
            if i >= max_lines:
                break

            parts = line.split()
            if len(parts) > 6:
                requests.append(parts[6])

    return requests


def normalize_requests(requests):
    mapping = {}
    normalized = []
    counter = 0

    for r in requests:
        if r not in mapping:
            mapping[r] = counter
            counter += 1
        normalized.append(mapping[r])

    return normalized