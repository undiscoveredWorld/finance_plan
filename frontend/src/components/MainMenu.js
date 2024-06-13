import MainMenuElement from "./MainMenuElement";

const MainMenu = (
    {
        buysOnClick = () => {},
        reportsOnClick = () =>  {}
    }) => {
    return <div className="main-menu">
        <MainMenuElement name="Buys" onClick={buysOnClick}/>
        <MainMenuElement name="Reports" onClick={reportsOnClick}/>
    </div>
}

export default MainMenu