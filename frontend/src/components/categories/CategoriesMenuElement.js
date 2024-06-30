const CategoriesMenuElement = ({
    name = "",
    onClick = () => {}

}) => {
    return <div className="container clickable p-0 h-auto categories-menu-element" onClick={onClick}>
        <div className="row categories-menu-element-container h-auto m-0">
            <h1 className="my-auto">{name}</h1>
        </div>
    </div>
}

export default CategoriesMenuElement