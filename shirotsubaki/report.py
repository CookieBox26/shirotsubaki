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
        self.data['style'] = str(self.style)
        with open(out_html, 'w', encoding='utf8', newline='\n') as ofile:
            ofile.write(self.template.render(self.data))


class Report(ReportBase):
    """A class for creating simple reports.

    Example:
        ``` python
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
