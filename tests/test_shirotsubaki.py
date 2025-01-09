import shirotsubaki.report
import shirotsubaki.utils
import os


def test_lighten_color():
    color = shirotsubaki.utils.lighten_color('#336699')
    assert color == '#99B2CC'


def test_report():
    report = shirotsubaki.report.Report()
    report.style.set('body', 'color', 'orange')
    report.set('title', 'xxxxxx')
    report.set('content', 'yyyyyy')
    report.output('my_report.html')
    os.remove('my_report.html')


def test_report_with_tabs():
    report = shirotsubaki.report.ReportWithTabs()
    report.set('title', 'xxxxxx')
    report.set_tab('apple', 'apple apple')
    report.set_tab('banana', 'banana banana')
    report.set_tab('cherry', 'cherry cherry')
    report.output('my_report_with_tabs.html')
    os.remove('my_report_with_tabs.html')
