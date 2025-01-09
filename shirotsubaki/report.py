from abc import ABC, abstractmethod
from jinja2 import Environment, FileSystemLoader, meta
import importlib.resources


class Style(dict):
    def __init__(self, d) -> None:
        super().__init__(d)

    def set(self, element: str, property: str, value: str) -> None:
        if element not in self:
            self[element] = {}
        self[element][property] = value

    def __str__(self) -> str:
        s = ''
        for k, v in self.items():
            s += k + ' {\n'
            for k_, v_ in v.items():
                s += f'  {k_}: {v_};\n'
            s += '}\n'
        return s[:-1]


class ReportBase(ABC):
    @abstractmethod
    def __init__(self) -> None:
        template_dir = importlib.resources.files('shirotsubaki').joinpath('templates')
        self.env = Environment(loader=FileSystemLoader(template_dir))
        self.style = Style({
            'body': {
                'margin': '15px',
                'color': '#303030',
                'font-family': '\'Verdana\', \'BIZ UDGothic\', sans-serif',
                'font-size': '90%',
                'line-height': '1.3',
                'letter-spacing': '0.02em',
            },
            'table': {
                'border-collapse': 'collapse',
            },
        })
        self.data = {}

    def set(self, key, value) -> None:
        self.data[key] = value

    def output(self, out_html) -> None:
        self.data['_style'] = str(self.style)
        with open(out_html, 'w', encoding='utf8', newline='\n') as ofile:
            ofile.write(self.template.render(self.data))


class Report(ReportBase):
    """A class for creating a simple report.

    Example:
        ```python
        import shirotsubaki.report

        report = shirotsubaki.report.Report()
        report.style.set('body', 'color', 'red')
        report.set('title', 'xxxxxx')
        report.set('content', 'yyyyyy')
        report.output('my_report.html')
        ```
    """
    def __init__(self) -> None:
        super().__init__()
        self.template = self.env.get_template('report.html')


class ReportWithTabs(ReportBase):
    """A class for creating a report with tabs.

    Example:
        ```python
        import shirotsubaki.report

        report = shirotsubaki.report.ReportWithTabs()
        report.set('title', 'xxxxxx')
        report.set_tab('apple', 'apple apple')
        report.set_tab('banana', 'banana banana')
        report.set_tab('cherry', 'cherry cherry')
        report.output('my_report_with_tabs.html')
        ```
    """
    def __init__(self) -> None:
        super().__init__()
        self.template = self.env.get_template('report_with_tabs.html')
        self.style.set('body', 'margin', '0')
        self.tabs = {}
        self.set('tabs', self.tabs)

    def set_tab(self, key, value) -> None:
        self.tabs[key] = value

    def _create_elements(self) -> None:
        selectors_comb = []
        selectors_has = []
        elements_radio = []
        elements_label = []
        for i, label in enumerate(self.tabs):
            selectors_comb.append(f'#btn{i:02}:checked ~ #tab{i:02}')
            selectors_has.append(f':has(#btn{i:02}:checked) .header label[for="btn{i:02}"]')
            elements_radio.append(f'<input type="radio" name="tab" id="btn{i:02}" hidden>')
            elements_label.append(f'<label for="btn{i:02}">{label}</label>')
        elements_radio[0] = elements_radio[0].replace('hidden', 'hidden checked')
        self.set('selectors_comb', ',\n'.join(selectors_comb))
        self.set('selectors_has', ',\n'.join(selectors_has))
        self.set('elements_radio', '\n'.join(elements_radio))
        self.set('elements_label', '\n'.join(elements_label))

    def output(self, out_html) -> None:
        self._create_elements()
        super().output(out_html)
