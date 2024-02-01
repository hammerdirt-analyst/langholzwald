# projet langholzli
# ersimann roger at hammerdirt

import pandas as pd


header_row = {'selector': 'th:nth-child(1)', 'props': 'background-color: #FFF; white-space: nowrap; word-break: keep-all;'}
even_rows = {"selector": 'tr:nth-child(even)', 'props': 'background-color: rgba(139, 69, 19, 0.08);'}
odd_rows = {'selector': 'tr:nth-child(odd)', 'props': 'background: #FFF;'}
table_font = {'selector': 'tr', 'props': 'font-size: 14px; padding:6px;'}
t_data = {'selector': 'td', 'props': 'padding:4px; text-align: center;'}
caption_bottom = {
    'selector': 'caption',
    'props': 'caption-side: bottom; font-size:14px; text-align: left; margin-top:14px;'
}
caption_top = {'selector': 'caption','props': 'caption-side: top; font-size:12px; text-align: left; margin-top:12px;'}
table_css_styles = [even_rows, odd_rows, table_font, header_row, t_data, caption_bottom]
table_css_styles_top = [even_rows, odd_rows, table_font, header_row, caption_top]

# the formatting for pd.styler
format_kwargs = dict(precision=2, thousands="'", decimal=",")

def add_table_to_page(table, table_no, caption, section, page: str = "", rule: str = "", format_index: str = 'both',
                      format_kwargs: dict = format_kwargs) -> pd.DataFrame:
    """
    Ajoute un tableau à une page dans un document.

    Cette fonction prend un tableau et ajoute son contenu à une page spécifique dans un document.
    Elle permet également de formater les en-têtes du tableau en majuscules si nécessaire.

    Args:
        table (pd.DataFrame): Le tableau à ajouter à la page.
        table_no (int): Le numéro du tableau.
        caption (str): La légende du tableau.
        section (str): La section du document.
        page (int): Le numéro de la page.
        rule (str): La règle du tableau.
        format_index (str, optional): Le format à appliquer aux en-têtes du tableau (par défaut 'both').
            - 'both' : Appliquer le format aux en-têtes des lignes et des colonnes.
            - 'columns' : Appliquer le format aux en-têtes des colonnes uniquement.
            - 'index' : Appliquer le format aux en-têtes des lignes uniquement.

    Returns:
        pd.DataFrame: Le tableau formaté avec la légende spécifiée et prêt à être ajouté au document.
    """
    caption = f'<b>Table {section}{page}-{table_no} :</b> {caption} {rule}'
    if format_index == 'both':
        table = table.format_index(str.capitalize, axis=1).format_index(str.capitalize, axis=0).format(**format_kwargs)
    if format_index == 'columns':
        table = table.format_index(str.capitalize, axis=1).format(**format_kwargs)
    if format_index == 'index':
        table = table.format_index(str.capitalize, axis=0).format(**format_kwargs)
    
    return table.set_caption(caption)