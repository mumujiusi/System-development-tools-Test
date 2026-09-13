import pytest

from greetlab.cli import main


def test_normal_name(monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["sdt-greet", "--name", "Alice"])
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, Alice!"


def test_blank_name_exits_2(monkeypatch):
    monkeypatch.setattr("sys.argv", ["sdt-greet", "--name", "   "])
    with pytest.raises(SystemExit) as excinfo:
        main()
    assert excinfo.value.code == 2
