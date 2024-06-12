import TableRow from "./TableRow";

const Table = () => {
    return <table className="w-100">
        <thead>
            <tr className="table-title">
                <td colSpan={5}><h1 className="text-center">Buys</h1></td>
            </tr>
            <tr className="table-header">
                <td id="1" className="table-header-col"><h2 className="text-center">Date</h2></td>
                <td id="2" className="table-header-col"><h2 className="text-center">Category</h2></td>
                <td id="3" className="table-header-col"><h2 className="text-center">Subcategory</h2></td>
                <td id="4" className="table-header-col"><h2 className="text-center">Product</h2></td>
                <td id="5" className="table-header-col"><h2 className="text-center">Summary</h2></td>
            </tr>
        </thead>
        <tbody>
            <TableRow />
            <TableRow />
        </tbody>
        <tbody>
        </tbody>
    </table>
}

export default Table