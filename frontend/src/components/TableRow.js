const TableRow = (props) => {
    const row = props.row
    const setterSelectedRow = props.setterSelectedRow
    const selectedRows = props.selectedRows

    let onClick = () => {
    }
    if (setterSelectedRow !== undefined) {
        onClick = () => {
            setterSelectedRow([...selectedRows, row.id])
        }
    }

    return (
        <tr onClick={onClick}>
            <td>{row.date}</td>
            <td>{row.category === {} ? "" : row.category.name}</td>
            <td>{row.subcategory === {} ? "" : row.subcategory.name}</td>
            <td>{row.product}</td>
            <td>{row.sum === -1 ? "" : row.sum}</td>
        </tr>
    )
}

export default TableRow
