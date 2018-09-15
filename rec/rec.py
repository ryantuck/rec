import petl


def sorted_table(t):
    sorted_headers = sorted(t.header())
    return t.cut(sorted_headers).sort(key=sorted_headers)


def same_row_count(t1, t2):
    return len(t1) == len(t2)


def diff_headers(t1, t2):
    t1_headers = set(t1.header())
    t2_headers = set(t2.header())
    return (sorted(t1_headers - t2_headers), sorted(t2_headers - t1_headers))


def diff_rows(t1, t2):
    return [(r1, r2) for r1, r2 in zip(t1, t2) if r1 != r2]


def reconcile_tables(t1, t2):
    issues = {}
    row_lengths = (len(t1), len(t2))
    header_diff = diff_headers(t1, t2)

    if len(set(row_lengths)) > 1:
        issues['row_lengths'] = row_lengths
        return issues

    if any(len(x) > 0 for x in header_diff):
        issues['header_diff'] = header_diff
        return issues

    rows_diff = diff_rows(t1, t2)
    if rows_diff != []:
        issues['rows_diff'] = rows_diff
        return issues
    return issues


def reconcile_csvs(csv_path_1, csv_path_2):
    t1 = sorted_table(petl.fromcsv(csv_path_1))
    t2 = sorted_table(petl.fromcsv(csv_path_2))
    return reconcile_tables(t1, t2)
