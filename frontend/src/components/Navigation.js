const Navigation = ({buysOnClick, reportsOnClick, categoriesOnClick}) => {
    return <div className="d-flex flex-nowrap" id="nav-container">
        <h2 className="col-auto clickable align-self-end" onClick={buysOnClick}>Buys</h2>
        <h2 className="col-auto clickable align-self-end" onClick={reportsOnClick}>Reports</h2>
        <h2 className="col-auto clickable align-self-end" onClick={categoriesOnClick}>Categories</h2>
    </div>
}

export default Navigation