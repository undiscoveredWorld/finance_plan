import TableRow from "./TableRow";
import WritableTableRow from "./WritableTableRow";
import {is_array_equal_array} from "../utils";

const Table = (props) => {
    const mode = props.mode
    const selectedRows = props.selectedRows
    const setSelectedRows = props.setSelectedRows
    const rows = props.rows

    const select_and_get_row = (row_data) => {
        if (mode === "edit" && selectedRows.includes(row_data.id))
            return <WritableTableRow row={row_data} key={row_data.id}/>
        else if (mode === "edit" && is_array_equal_array(selectedRows, []))
            return <TableRow row={row_data} key={row_data.id} setterSelectedRow={setSelectedRows}
                             selectedRows={selectedRows}/>
        return <TableRow row={row_data} key={row_data.id}/>
    }

    const listRows = rows.map(select_and_get_row)
    return (
        <table className="w-100">
            <thead>
            <tr className="table-title">
                <td colSpan={5}><h1 className="text-center">Buys</h1></td>
            </tr>
            <tr className="table-header">
                <td className="table-header-col"><h2 className="text-center">Date</h2></td>
                <td className="table-header-col"><h2 className="text-center">Category</h2></td>
                <td className="table-header-col"><h2 className="text-center">Subcategory</h2></td>
                <td className="table-header-col"><h2 className="text-center">Product</h2></td>
                <td className="table-header-col"><h2 className="text-center">Sum</h2></td>
            </tr>
            </thead>
            <tbody>
            {listRows}
            </tbody>
            <tbody>
            </tbody>
        </table>
    )
}

export default Table