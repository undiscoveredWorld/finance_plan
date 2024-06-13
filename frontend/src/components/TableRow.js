const TableRow = ({
                      writable=false,
                      date = "",
                      category = {},
                      subcategory = {},
                      product = "",
                      summary = -1,}) => {
    if (writable) {
        return <tr className="writable_row">
            <td><input type="text"/>{date}</td>
            <td><input type="text"/>{category}</td>
            <td><input type="text"/>{subcategory}</td>
            <td><input type="text"/>{product}</td>
            <td><input type="text"/>{summary}</td>
        </tr>
    }
    return <tr>
        <td>{date}</td>
        <td>{category === {} ? "" : category.name}</td>
        <td>{subcategory === {} ? "" : subcategory.name}</td>
        <td>{product}</td>
        <td>{summary === -1 ? "" : summary}</td>
    </tr>
}


export default TableRow
