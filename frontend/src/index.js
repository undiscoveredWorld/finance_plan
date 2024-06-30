import {createRoot} from "react-dom/client";
import {useState} from "react";

import './css/common.css'
import './css/header.css'
import './css/main-menu.css'
import './css/buys.css'
import './css/button.css'
import './css/categories.css'

import Header from './components/Header'
import Main from "./components/Main";
import {MenuManager} from "./utils";

const App = () => {
    const [openedMenu, setOpenedMenu] = useState("Main menu")
    const menuManager = new MenuManager(setOpenedMenu)

    return (
        <>
            <Header menuManager={menuManager}/>
            <Main menuManager={menuManager} openedMenu={openedMenu}/>
        </>
    )
}

const root = createRoot(document.getElementById('app'))
root.render(<App/>)