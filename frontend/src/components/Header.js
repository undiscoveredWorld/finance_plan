const Header = () => {
    return <header>
        <div className="d-flex flex-nowrap w-100" id="header-container">
            <div className="site-name col-auto align-self-start m-0">
                Finance plan
            </div>
            <div className="col w-100"></div>
            <nav className="col-auto align-self-end">
                <div className="d-flex flex-nowrap" id="nav-container">
                    <h2 className="col-auto align-self-end">Buys</h2>
                    <h2 className="col-auto align-self-end">Reports</h2>
                </div>
            </nav>
        </div>
    </header>
}

export default Header