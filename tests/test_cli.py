from tennis_results_dashboard import cli


def test_main_prints_message(capsys):
    cli.main()
    captured = capsys.readouterr()
    assert "Hello from the Tennis Results Dashboard!" in captured.out
