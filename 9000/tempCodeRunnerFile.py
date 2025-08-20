    last = local_arr[-1]
        for check_idx, check in enumerate(local_arr[:-1]):
            dist = idx - check_idx
            if check + dist == last or check - dist == last:
                return