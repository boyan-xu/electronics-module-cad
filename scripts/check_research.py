"""Read-only research table check; Python standard library only."""
import argparse
from collections import Counter
import csv
import math
from pathlib import Path

SCHEMAS = {
    'sources': 'id url revision path sha256 status reason',
    'packages': 'id part variant length_mm width_mm height_mm lead_extents source status',
    'components': 'ref side x_mm y_mm rotation_deg package source status',
    'pins': 'connector number signal x_mm y_mm z_mm view source status',
}


def check(root):
    errors, tables, counts = [], {}, Counter()
    unresolved = 0
    for name, schema in SCHEMAS.items():
        rows = []
        try:
            with (root / (name + '.csv')).open(encoding='utf-8-sig', newline='') as stream:
                reader = csv.DictReader(stream, strict=True)
                if reader.fieldnames != schema.split():
                    errors.append(f'{name}: incorrect header')
                    tables[name] = []
                    continue
                rows = list(reader)
        except (OSError, UnicodeError, csv.Error) as exc:
            errors.append(f'{name}: cannot read table ({type(exc).__name__})')
        tables[name] = rows
        counts[name] = len(rows)
        seen = set()
        for line, raw in enumerate(rows, 2):
            label = f'{name}:{line}'
            if None in raw or any(value is None for value in raw.values()):
                errors.append(f'{label}: ragged row')
                continue
            row = {key: value.strip() for key, value in raw.items()}
            raw.update(row)
            keys = ('connector', 'number') if name == 'pins' else (schema.split()[0],)
            identity = tuple(row[k] for k in keys)
            if identity in seen:
                errors.append(f'{label}: duplicate identity {identity}')
            seen.add(identity)
            optional = {'revision', 'path', 'sha256'} if name == 'sources' else set()
            for field, value in row.items():
                if not value and field not in optional:
                    errors.append(f'{label}: missing {field}')
                if field.endswith(('_mm', '_deg')):
                    try:
                        number = float(value)
                        if not math.isfinite(number) or (field in ('length_mm', 'width_mm', 'height_mm') and number <= 0):
                            raise ValueError
                    except ValueError:
                        errors.append(f'{label}: invalid {field}')
            allowed = {'adopted', 'reference', 'rejected', 'blocked', 'unverified'} if name == 'sources' else {'verified', 'missing', 'unverified', 'conflict'}
            if row['status'] not in allowed:
                errors.append(f'{label}: invalid status')
            if name != 'sources' and row['status'] != 'verified':
                unresolved += 1
            if name == 'components' and row['side'] not in ('top', 'bottom'):
                errors.append(f'{label}: invalid side')
            if name == 'sources':
                digest = row['sha256']
                if row['path'] and not digest:
                    errors.append(f'{label}: downloaded file needs sha256')
                if digest and (len(digest) != 64 or any(c not in '0123456789abcdefABCDEF' for c in digest)):
                    errors.append(f'{label}: invalid sha256')
    sources = {r.get('id'): r.get('status') for r in tables['sources']}
    packages = {r.get('id'): r.get('status') for r in tables['packages']}
    for name in ('packages', 'components', 'pins'):
        for line, row in enumerate(tables[name], 2):
            source = row.get('source')
            if source not in sources:
                errors.append(f'{name}:{line}: unknown source {source}')
            elif row.get('status') == 'verified' and sources[source] != 'adopted':
                errors.append(f'{name}:{line}: verified entry needs adopted source')
            if name == 'components':
                package = row.get('package')
                if package not in packages:
                    errors.append(f'{name}:{line}: unknown package {package}')
                elif row.get('status') == 'verified' and packages[package] != 'verified':
                    errors.append(f'{name}:{line}: package is unresolved')
    for name in ('sources', 'packages', 'components'):
        if not tables[name]:
            errors.append(f'{name}: empty table')
    return counts, unresolved, errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('directory', type=Path)
    parser.add_argument('--details', action='store_true', help='show field and reference errors')
    args = parser.parse_args()
    counts, unresolved, errors = check(args.directory)
    print('Research tables: ' + ', '.join(f'{name}={counts[name]}' for name in SCHEMAS))
    print(f'errors={len(errors)}, unresolved={unresolved}; not CAD verification or a completeness certificate.')
    if args.details:
        print('\n'.join(errors) or 'No table errors.')
    return 1 if errors or unresolved else 0


if __name__ == '__main__':
    raise SystemExit(main())
