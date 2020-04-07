import pathlib
import pytest
import cv2
import time
import pupil_apriltags


@pytest.mark.parametrize(
    "family,num_markers",
    [
        ("tag16h5", 30),
        ("tag25h9", 35),
        ("tag36h11", 587),
        ("tagCircle21h7", 38),
        pytest.param("tagCircle49h12", 65535, marks=pytest.mark.slow),
        pytest.param("tagCustom48h12", 42211, marks=pytest.mark.slow),
        pytest.param("tagStandard41h12", 2115, marks=pytest.mark.slow),
        pytest.param("tagStandard52h13", 48714, marks=pytest.mark.slow),
    ],
)
def test_familiy(family, num_markers):
    t0 = time.perf_counter_ns()
    detector = pupil_apriltags.Detector(families=family)
    time_init = (time.perf_counter_ns() - t0) / 1_000_000
    cwd = pathlib.Path(__file__).parent
    img_path = cwd / "images" / f"{family}.png"
    img = cv2.imread(str(img_path))
    assert img is not None, f"Image not found at {img_path}"
    assert img.size > 0
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    t0 = time.perf_counter_ns()
    markers = detector.detect(img)
    time_detect = (time.perf_counter_ns() - t0) / 1_000_000
    print(family, time_init, len(markers), time_detect)
    assert len(markers) == num_markers
