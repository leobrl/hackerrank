from bisect import bisect_left
import pytest


def activity_notifications(ts: list[int], w: int) -> int:
    """Counts how many values are larger or equal than the median for the previous period w.
    The first w numbers are not part of the check.

    Args:
        ts (list[int]): a list of integers
        w (int): the width of the window

    Returns:
        int: the number of time a value is larger or equal to the mean.
    """

    is_even = w % 2 == 0

    def calc_median(q):
        m = w // 2
        return (q[m] + q[m - 1]) / 2 if is_even else q[m]

    queue = sorted(ts[:w])
    median, res = calc_median(queue), 0
    for i, e in enumerate(ts[w:], start=0):
        if e >= 2.0 * median:
            res += 1

        _ = queue.pop(bisect_left(queue, ts[i]))
        queue.insert(bisect_left(queue, e), e)

        median = calc_median(queue)

    return res


@pytest.mark.parametrize(
    "ts, w, expected", [([2, 3, 4, 2, 3, 6, 8, 4, 5], 5, 2), ([1, 2, 3, 4, 4], 4, 0)]
)
def test_activity_notification(ts, w, expected):
    actual = activity_notifications(ts, w)
    assert actual == expected


# Run test from cmd:
# python -m pytest ./Activity_Notification/activity_notification.py
