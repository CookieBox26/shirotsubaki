import shirotsubaki.report
import shirotsubaki.utils


def test_lighten_color():
    color = shirotsubaki.utils.lighten_color('#336699')
    assert color == '#99B2CC'


def test_report():
    shirotsubaki.report.Report()
