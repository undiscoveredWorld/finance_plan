const TableRow = ({
                      writable=false,
                      date = "",
                      category = {},
                      subcategory = {},
                      product = "",
                      summary = -1}) => {
    return <tr className={writable ? "writable-row" : ""}>
        <td>{date}</td>
        <td>{category === {} ? "" : category.name}</td>
        <td>{subcategory === {} ? "" : subcategory.name}</td>
        <td>{product}</td>
        <td>{summary === -1 ? "" : summary}</td>
    </tr>
}


export default TableRow
