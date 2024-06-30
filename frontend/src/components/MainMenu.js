import MenuElement from "./MenuElement";
import {empty_func} from "../utils";

const MainMenu = (props) => {
    const menuManager = props.menuManager

    return (
        <div className="main-menu">
            <MenuElement name="Buys" onClick={menuManager.openBuys}/>
            <MenuElement name="Reports" onClick={empty_func}/>
            <MenuElement name="Categories" onClick={menuManager.openCategories}/>
        </div>
    )
}

export default MainMenu