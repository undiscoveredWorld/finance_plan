import Category from "./Category";
import SubcategoriesList from "./SubcategoriesList";

const CategoryList = (props) => {
    const categories = props.categories
    const selectCursor = props.selectCursor
    const setSelectCursor = props.setSelectCursor

    const render_category = (category) => {
        return (
            <div className="category-container" key={category.id}>
                <Category name={category.name === "" ? "Default" : category.name} category_id={category.id}
                          selectCursor={selectCursor} setSelectCursor={setSelectCursor}/>
                <SubcategoriesList subcategories={category.subcategories} category_id={category.id}
                                   selectCursor={selectCursor} setSelectCursor={setSelectCursor}/>
            </div>
        )
    }

    return (
        <div className="list">
            {categories.map(render_category)}
        </div>
    )
}

export default CategoryList