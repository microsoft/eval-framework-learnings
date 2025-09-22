from evalproj import cli


def test_cli_defaults(capsys):
    cli.main([])
    captured = capsys.readouterr()
    assert "Hello, World!" in captured.out


def test_cli_name(capsys):
    cli.main(["--name", "Alice"])
    captured = capsys.readouterr()
    assert "Hello, Alice!" in captured.out
