import MainMenu from "./MainMenu";
import Buys from "./Buys";
import Categories from "./categories/Categories";

const Main = (props) => {
    const openedMenu = props.openedMenu
    const menuManager = props.menuManager

    const openMenu = (menuName) => {
        if (menuName === "Main menu") {
            return <MainMenu menuManager={menuManager}/>
        } else if (menuName === "Buys") {
            return <Buys/>
        } else if (menuName === "Categories") {
            return <Categories/>
        }
    }

    return (
        <div className="container pt-0 px-0" id="main">
            {openMenu(openedMenu)}
        </div>
    )
}

export default Main