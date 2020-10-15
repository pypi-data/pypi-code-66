import hypothesis.strategies
import strax.testutils

import numpy as np
import strax


@hypothesis.given(strax.testutils.sorted_intervals,
                  strax.testutils.disjoint_sorted_intervals)
@hypothesis.settings(deadline=None)
# Tricky example: uncontained interval precedes contained interval
# (this did not produce an issue, but good to show this is handled)
@hypothesis.example(
    things=np.array([(0, 1, 1, 0),
                     (1, 5, 1, 0),
                     (2, 1, 1, 0)],
                    dtype=strax.interval_dtype),
    containers=np.array([(0, 4, 1, 0)],
                        dtype=strax.interval_dtype))
def test_fully_contained_in(things, containers):
    result = strax.fully_contained_in(things, containers)

    assert len(result) == len(things)
    if len(result):
        assert result.max() < len(containers)

    for i, thing in enumerate(things):
        if result[i] == -1:
            # Check for false negative
            for c in containers:
                assert not _is_contained(thing, c)
        else:
            # Check for false positives
            assert _is_contained(thing, containers[result[i]])


@hypothesis.given(strax.testutils.sorted_intervals,
                  strax.testutils.disjoint_sorted_intervals,
                  hypothesis.strategies.integers(-2, 2))
@hypothesis.settings(deadline=None)
@hypothesis.example(
    things=np.array([(0, 1, 1, 0),
                     (1, 5, 1, 0),
                     (2, 1, 1, 0)],
                    dtype=strax.interval_dtype),
    containers=np.array([(0, 4, 1, 0)],
                        dtype=strax.interval_dtype),
    window=0)
def test_touching_windows(things, containers, window):
    result = strax.touching_windows(things, containers, window=window)
    assert len(result) == len(containers)
    if len(result):
        assert np.all((0 <= result) & (result <= len(things)))

    for c_i, container in enumerate(containers):
        i_that_touch = np.arange(*result[c_i])
        for t_i, thing in enumerate(things):
            if (strax.endtime(thing) <= container['time'] - window
                    or thing['time'] >= strax.endtime(container) + window):
                assert t_i not in i_that_touch
            else:
                assert t_i in i_that_touch


@hypothesis.settings(deadline=None, max_examples=1000)
@hypothesis.given(strax.testutils.sorted_intervals,
                  strax.testutils.disjoint_sorted_intervals)
# Specific example to trigger issue #37
@hypothesis.example(
    things=np.array([(2, 1, 1, 0)],
                    dtype=strax.interval_dtype),
    containers=np.array([(0, 1, 1, 0), (2, 1, 1, 0)],
                        dtype=strax.interval_dtype))
def test_split_by_containment(things, containers):
    result = strax.split_by_containment(things, containers)

    assert len(result) == len(containers)

    for container_i, things_in in enumerate(result):
        for t in things:
            assert ((t in things_in)
                    == _is_contained(t, containers[container_i]))

    if len(result) and len(np.concatenate(result)) > 1:
        assert np.diff(np.concatenate(result)['time']).min() >= 0, "Sorting bug"


def _is_contained(_thing, _container):
    # Assumes dt = 1
    return _container['time'] \
           <= _thing['time'] \
           <= _thing['time'] + _thing['length'] \
           <= _container['time'] + _container['length']


@hypothesis.settings(deadline=None)
@hypothesis.given(strax.testutils.several_fake_records,
                  hypothesis.strategies.integers(0, 50),
                  hypothesis.strategies.booleans())
def test_split_array(data, t, allow_early_split):
    print(f"\nCalled with {np.transpose([data['time'], strax.endtime(data)]).tolist()}, "
          f"{t}, {allow_early_split}")

    try:
        data1, data2, tsplit = strax.split_array(
            data, t, allow_early_split=allow_early_split)

    except strax.CannotSplit:
        assert not allow_early_split
        # There must be data straddling t
        for d in data:
            if d['time'] < t < strax.endtime(d):
                break
        else:
            raise ValueError("threw CannotSplit needlessly")

    else:
        if allow_early_split:
            assert tsplit <= t
            t = tsplit

        assert len(data1) + len(data2) == len(data)
        assert np.all(strax.endtime(data1) <= t)
        assert np.all(data2['time'] >= t)


@hypothesis.settings(deadline=None)
@hypothesis.given(strax.testutils.several_fake_records)
def test_from_break(records):
    if not len(records):
        return

    window = 5

    def has_break(x):
        if len(x) < 2:
            return False
        for i in range(1, len(x)):
            if strax.endtime(x[:i]).max() + window <= x[i]['time']:
                return True
        return False

    try:
        left, t_break_l = strax.from_break(records, safe_break=window,
                                           left=True, tolerant=False)
        right, t_break_r = strax.from_break(records, safe_break=window,
                                            left=False, tolerant=False)
    except strax.NoBreakFound:
        assert not has_break(records)

    else:
        assert t_break_l == t_break_r, "Inconsistent break time"
        t_break = t_break_l

        assert has_break(records), f"Found nonexistent break at {t_break}"

        assert len(left) + len(right) == len(records), "Data loss"

        if len(records) > 0:
            np.testing.assert_equal(np.concatenate([left, right]),
                                    records)
        if len(right) and len(left):
            assert t_break == right[0]['time']
            assert strax.endtime(left).max() <= right[0]['time'] - window
        assert not has_break(right)


@hypothesis.settings(deadline=None)
@hypothesis.given(
    hypothesis.strategies.integers(0, 100),
    hypothesis.strategies.integers(0, 100),
    hypothesis.strategies.integers(0, 100),
    hypothesis.strategies.integers(0, 100))
def test_overlap_indices(a1, n_a, b1, n_b):
    a2 = a1 + n_a
    b2 = b1 + n_b

    (a_start, a_end), (b_start, b_end) = strax.overlap_indices(a1, n_a, b1, n_b)
    assert a_end - a_start == b_end - b_start, "Overlap must be equal length"
    assert a_end >= a_start, "Overlap must be nonnegative"

    if n_a == 0 or n_b == 0:
        assert a_start == a_end == b_start == b_end == 0
        return

    a_filled = np.arange(a1, a2)
    b_filled = np.arange(b1, b2)
    true_overlap = np.intersect1d(a_filled, b_filled)
    if not len(true_overlap):
        assert a_start == a_end == b_start == b_end == 0
        return

    true_a_inds = np.searchsorted(a_filled, true_overlap)
    true_b_inds = np.searchsorted(b_filled, true_overlap)

    found = (a_start, a_end), (b_start, b_end)
    expected = (
        (true_a_inds[0], true_a_inds[-1] + 1),
        (true_b_inds[0], true_b_inds[-1] + 1))
    assert found == expected
