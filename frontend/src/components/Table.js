import TableRow from "./TableRow";
import WritableTableRow from "./WritableTableRow";
import {is_array_equal_array} from "../utils";

const Table = (props) => {
    const listRows = props.rows.map((row) => {
        if (props.mode === "edit" && props.selectedRows.includes(row.id))
            return <WritableTableRow row={row} key={row.id} />
        else if (props.mode === "edit" && is_array_equal_array(props.selectedRows, []))
            return <TableRow row={row} key={row.id} setterSelectedRow={props.setSelectedRows} selectedRows={props.selectedRows}/>
        return <TableRow row={row} key={row.id}/>
    })
    return <table className="w-100">
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
}

export default Table