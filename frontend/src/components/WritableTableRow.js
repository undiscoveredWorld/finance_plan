import {useState} from "react";

import WritableTD from "./WritableTD";

const WritableTableRow = (props) => {
    const row_data = props.row
    const [date, setDate] = useState(row_data.date)
    const [category_name, setCategoryName] = useState(row_data.category === {} ? "" : row_data.category.name)
    const [subcategory_name, setSubcategoryName] = useState(row_data.subcategory === {} ? "" : row_data.subcategory.name)
    const [product, setProduct] = useState(row_data.product)
    const [sum, setSum] = useState(row_data.sum === -1 ? "" :row_data.sum)

    return (
        <tr className="writable_row">
            <WritableTD default_value={date} setter={setDate} />
            <WritableTD default_value={category_name} setter={setCategoryName} />
            <WritableTD default_value={subcategory_name} setter={setSubcategoryName} />
            <WritableTD default_value={product} setter={setProduct} />
            <WritableTD default_value={sum} setter={setSum} />
        </tr>
    )
}

export default WritableTableRow