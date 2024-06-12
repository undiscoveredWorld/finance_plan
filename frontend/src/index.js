import {createRoot} from "react-dom/client";

import './css/common.css'
import './css/header.css'
import './css/main-menu.css'
import './css/table.css'
import './css/button.css'

import Header from './components/Header'
import MainMenuElement from "./components/MainMenuElement";
import Table from "./components/Table";
import Button from "./components/Button";

const App = () => {
    return <>
<Header />
<div className="container pt-0 px-0" id="main">
    <div className="main-menu">
        <MainMenuElement name="Buys"/>
        <MainMenuElement name="Reports"/>
    </div>
    <div className="buys-table d-flex flex-nowrap w-100 my-4">
        <div className="col w-100"></div>
        <h2>Select the row</h2>
        <Button name="Edit"/>
        <Button name="Delete"/>
        <Button name="Cancel" enabled={false}/>
    </div>
    <Table />
</div>
    </>
}

const root = createRoot(document.getElementById('app'))
root.render(<App />)