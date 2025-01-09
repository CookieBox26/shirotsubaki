# Examples

Here are some examples of how to use this package:

## Example 1

<a href="../example_1.html" class="asis" target="_blank" rel="noopener noreferrer">example_1.html</a>

```python
import shirotsubaki.report
from shirotsubaki.element import Element as Elm

def create_table():
    tbl = Elm('table')
    thead = Elm('thead')
    tbody = Elm('tbody')

    thead.append(Elm('tr'))
    for _ in range(5):
        thead.inner[-1].append(Elm('th', 'apple'))
        thead.inner[-1].append(Elm('th', 'banana'))
        thead.inner[-1].append(Elm('th', 'cherry'))
    for i in range(20):
        tbody.append(Elm('tr'))
        for _ in range(5):
            tbody.inner[-1].append(Elm('td', 'apple'))
            tbody.inner[-1].append(Elm('td', 'banana'))
            tbody.inner[-1].append(Elm('td', 'cherry'))

    tbl.append(thead)
    tbl.append(tbody)
    div = Elm('div', tbl).set_attr('class', 'table-container')
    return div

report = shirotsubaki.report.Report()
report.style.add_scrollable_table()
report.set('title', 'Fruits')
report.append_to('content', Elm('h1', 'Fruits'))
report.append_to('content', create_table())
report.output('docs/example_1.html')
```
