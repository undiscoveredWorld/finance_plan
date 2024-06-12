const MainMenuElement = (props) => {
    return <div className="container p-0 h-auto main-menu-element">
        <div className="row main-menu-element-container h-auto m-0">
            <h1 className="my-auto">{props.name}</h1>
        </div>
    </div>
}

export default MainMenuElement