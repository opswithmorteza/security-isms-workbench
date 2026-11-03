"""Validate a sample risk register and calculate transparent risk scores."""
import csv
import json
import sys

REQUIRED = {'id', 'asset', 'risk', 'likelihood', 'impact', 'owner', 'treatment'}


def assess(row):
    missing = [k for k in REQUIRED if not str(row.get(k, '')).strip()]
    if missing:
        raise ValueError('Missing fields: ' + ', '.join(sorted(missing)))
    likelihood, impact = int(row['likelihood']), int(row['impact'])
    if not (1 <= likelihood <= 5 and 1 <= impact <= 5):
        raise ValueError('Likelihood and impact must be integers from 1 to 5.')
    score = likelihood * impact
    level = 'critical' if score >= 20 else 'high' if score >= 13 else 'medium' if score >= 6 else 'low'
    return {**row, 'score': score, 'level': level}


def load(path):
    with open(path, newline='', encoding='utf-8-sig') as stream:
        reader = csv.DictReader(stream)
        if not REQUIRED.issubset(reader.fieldnames or []):
            raise ValueError('CSV header is missing required columns.')
        result, seen = [], set()
        for line, row in enumerate(reader, 2):
            try:
                item = assess(row)
                if item['id'] in seen:
                    raise ValueError('Duplicate risk ID.')
                seen.add(item['id'])
                result.append(item)
            except (ValueError, TypeError) as error:
                raise ValueError(f'Line {line}: {error}') from error
    return sorted(result, key=lambda r: r['score'], reverse=True)


if __name__ == '__main__':
    try:
        print(json.dumps(load(sys.argv[1] if len(sys.argv) > 1 else 'sample-risks.csv'), indent=2))
    except (OSError, ValueError) as error:
        print(str(error), file=sys.stderr)
        raise SystemExit(1)
