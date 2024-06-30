import SiteName from "./SiteName";
import Navigation from "./Navigation";

const Header = (props) => {
    const menuManager = props.menuManager

    return (
        <header className="d-flex flex-nowrap w-100">
            <div className="d-flex flex-nowrap w-100">
                <SiteName titleOnClick={menuManager.openMainMenu}/>
                <div className="col w-100"></div>
                <Navigation menuManager={menuManager}/>
            </div>
        </header>
    )
}

export default Header