import SiteName from "./SiteName";
import Navigation from "./Navigation";

const Header = ({
                    titleOnClick = () => {},
                    buysOnClick = () => {},
                    reportsOnClick = () => {}
}) => {
    return <header>
        <div className="d-flex flex-nowrap w-100" id="header-container">
            <SiteName titleOnClick={titleOnClick}/>
            <div className="col w-100"></div>
            <nav className="col-auto align-self-end">
                <Navigation buysOnClick={buysOnClick} reportsOnClick={reportsOnClick()}/>
            </nav>
        </div>
    </header>
}

export default Header