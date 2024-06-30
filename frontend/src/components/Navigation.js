import {empty_func} from "../utils";

const Navigation = (props) => {
    const menuManager = props.menuManager
    const h2_className = "col-auto clickable align-self-end"

    return (
        <nav className="col-auto align-self-end">
            <div className="d-flex flex-nowrap" id="nav-container">
                <h2 className={h2_className} onClick={menuManager.openBuys}>Buys</h2>
                <h2 className={h2_className} onClick={empty_func}>Reports</h2>
                <h2 className={h2_className} onClick={menuManager.openCategories}>Categories</h2>
            </div>
        </nav>
    )
}

export default Navigation