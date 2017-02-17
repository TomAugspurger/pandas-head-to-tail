import pandas as pd
from IPython import display


def side_by_side(df1, df2, name1='', name2=''):
    if isinstance(df1, pd.Series):
        df1 = df1.to_frame(name=df1.name)
    if isinstance(df2, pd.Series):
        df2 = df2.to_frame(name=df2.name)
    inline = 'style="display: float; max-width:50%" class="table"'
    q = '''
    <div class="table-responsive col-md-6">{}</div>
    <div class="table-responsive col-md-6">{}</div>
    '''.format(df1.style.set_table_attributes(inline)
                  .set_caption(name1).render(),
               df2.style.set_table_attributes(inline)
                  .set_caption(name2).render())
    return display.HTML(q)


def join_date_time(df):

    def convert(col):
        s = (df[col].astype(str)
             .str.replace('\.0', '')
             .str.rjust(4, '0'))
        td = pd.to_timedelta(s.str.slice(0, 2) + 'H' +
                             s.str.slice(-2) + 'm',
                             errors='coerce')
        return df['fl_date'] + td

    return df.assign(dep=convert('dep_time'),
                     arr=convert('arr_time'))

def show(df, max_rows=75, max_cols=50):
    row = pd.option_context('display.max_rows', max_rows)
    col = pd.option_context('display.max_columns', max_cols)
    with row, col:
        display.display(df)
