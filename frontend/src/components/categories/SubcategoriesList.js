import Subcategory from "./Subcategory"
import CreateSubcategory from "./CreateSubcategory"

const SubcategoriesList = (props) => {
    const selectCursor = props.selectCursor
    const setSelectCursor = props.setSelectCursor
    const subcategories = props.subcategories
    const category_id = props.category_id

    const render_subcategory = (subcategory) => {
        if (subcategory.name !== "")
            return <Subcategory key={subcategory.id} name={subcategory.name}
                                category_id={category_id} subcategory_id={subcategory.id}
                                selectCursor={selectCursor} setSelectCursor={setSelectCursor}/>
    }

    return (
        <div className="list subcategories-list">
            <CreateSubcategory category_id={category_id}
                               selectCursor={selectCursor} setSelectCursor={setSelectCursor}/>
            {subcategories.map(render_subcategory)}
        </div>
    )
}

export default SubcategoriesList