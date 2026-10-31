"""The per-swath azimuth misregistration lookup shared by geo2rdr and resamp_withCarrier."""
import s1a_isce_utils as ut


def test_per_swath_file_wins_when_present(tmp_path):
    date = tmp_path / "20260909.txt"
    date.write_text("0.001\n")
    (tmp_path / "IW2").mkdir()
    (tmp_path / "IW2" / "20260909.txt").write_text("0.002\n")

    assert ut.swathMisregFile(str(date), 2) == str(tmp_path / "IW2" / "20260909.txt")
    assert ut.swathMisregFile(str(date), 1) == str(date)


def test_missing_and_default_paths_pass_through(tmp_path):
    assert ut.swathMisregFile(str(tmp_path / "none.txt"), 1) == str(tmp_path / "none.txt")
    # resamp_withCarrier's default for an absent option is the float 0.0
    assert ut.swathMisregFile(0.0, 1) == 0.0
