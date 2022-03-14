import json

from streamlit_elements import mui
from .dashboard import Dashboard


class DataGrid(Dashboard.Item):

    DEFAULT_COLUMNS = [
        { "field": 'id', "headerName": 'ID', "width": 90 },
        { "field": 'firstName', "headerName": 'First name', "width": 150, "editable": True, },
        { "field": 'lastName', "headerName": 'Last name', "width": 150, "editable": True, },
        { "field": 'age', "headerName": 'Age', "type": 'number', "width": 110, "editable": True, },
    ]
    DEFAULT_ROWS = [
        { "id": 1, "lastName": 'Snow', "firstName": 'Jon', "age": 35 },
        { "id": 2, "lastName": 'Lannister', "firstName": 'Cersei', "age": 42 },
        { "id": 3, "lastName": 'Lannister', "firstName": 'Jaime', "age": 45 },
        { "id": 4, "lastName": 'Stark', "firstName": 'Arya', "age": 16 },
        { "id": 5, "lastName": 'Targaryen', "firstName": 'Daenerys', "age": None },
        { "id": 6, "lastName": 'Melisandre', "firstName": None, "age": 150 },
        { "id": 7, "lastName": 'Clifford', "firstName": 'Ferrara', "age": 44 },
        { "id": 8, "lastName": 'Frances', "firstName": 'Rossini', "age": 36 },
        { "id": 9, "lastName": 'Roxie', "firstName": 'Harvey', "age": 65 },
    ]

    def _handle_edit(self, params):
        print(params)

    def __call__(self, json_data):
        data = json.loads(json_data)

        with mui.paper(key=self._key, sx={"display": "flex", "flexDirection": "column"}, elevation=3):
            with self.title_bar(padding="10px 15px 10px 15px", dark_switcher=False):
                mui.icon.ondemand_video()
                mui.typography("Data grid")

            with mui.box(sx={"flex": 1, "minHeight": 0}):
                mui.data_grid(
                    columns=self.DEFAULT_COLUMNS,
                    rows=data,
                    page_size=5,
                    rows_per_page_options=[5],
                    checkbox_selection=True,
                    disable_selection_on_click=True,
                    on_cell_edit_commit=self._handle_edit,
                )
