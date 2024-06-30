const MenuElement = ({
    name = "",
    onClick = () => {}

}) => {
    return <div className="container clickable p-0 h-auto menu-element" onClick={onClick}>
        <div className="row menu-element-container h-auto m-0">
            <h1 className="my-auto">{name}</h1>
        </div>
    </div>
}

export default MenuElement