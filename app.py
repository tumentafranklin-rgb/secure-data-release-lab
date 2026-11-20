def summarize_records(records):
    counts = {"received": 0, "processed": 0}

    for record in records:
        status = record.get("status")
        if status not in counts:
            raise ValueError(f"Unsupported record status: {status!r}")
        counts[status] += 1

    return counts


if __name__ == "__main__":
    records = [
        {"status": "received"},
        {"status": "processed"},
        {"status": "received"},
    ]
    print(summarize_records(records))