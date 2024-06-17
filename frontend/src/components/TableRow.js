const TableRow = (props) => {
    const row = props.row
    let onClick = () => {
    }
    if (props.setterSelectedRow !== undefined) {
        onClick = () => {
            props.setterSelectedRow([...props.selectedRows, props.row.id])
        }
    }

    return <tr onClick={onClick}>
        <td>{row.date}</td>
        <td>{row.category === {} ? "" : row.category.name}</td>
        <td>{row.subcategory === {} ? "" : row.subcategory.name}</td>
        <td>{row.product}</td>
        <td>{row.sum === -1 ? "" : row.sum}</td>
    </tr>
}

export default TableRow
