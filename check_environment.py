import importlib

packages = ['pandas', 'IPython', 'statsmodels', 'sklearn', 'seaborn',
            'toolz', 'requests', 'scipy']

bad = []
for package in packages:
    try:
        importlib.import_module(package)
    except ImportError:
        bad.append("Can't import %s" % package)
else:
    if len(bad) > 0:
        print('\n'.join(bad))
    else:
        try:
            import pandas as pd
            df = pd.read_csv("notebooks/data/cpi.csv")
            print("All good. Enjoy the tutorial!")
        except Exception as e:
            print("Couldn't read CPI")
            print(e)
