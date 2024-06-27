import MainMenuElement from "./MainMenuElement";

const MainMenu = (
    {
        buysOnClick = () => {},
        reportsOnClick = () =>  {},
        categoriesOnClick = () => {},
    }) => {
    return <div className="main-menu">
        <MainMenuElement name="Buys" onClick={buysOnClick}/>
        <MainMenuElement name="Reports" onClick={reportsOnClick}/>
        <MainMenuElement name="Categories" onClick={categoriesOnClick}/>
    </div>
}

export default MainMenu