import MainMenuElement from "./MainMenuElement"

const Reports = () => {
    return <>
    <div className="main-menu">
        <MainMenuElement name="Expenses by day"/>
        <MainMenuElement name="Expenses by categories"/>
        <MainMenuElement name="Remainder report"/>
    </div>
    </>
}

export default Reports