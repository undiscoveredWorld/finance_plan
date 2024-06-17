import {createRoot} from "react-dom/client";
import {useState} from "react";
import {useEffect} from "react";

import './css/common.css'
import './css/header.css'
import './css/main-menu.css'
import './css/table.css'
import './css/button.css'

import Header from './components/Header'
import MainMenu from "./components/MainMenu";
import Buys from "./components/Buys";

const App = () => {
    const [openedMenu, setOpenedMenu] = useState("Main menu")

    const openBuys = () => {
        setOpenedMenu("Buys")
    }

    const openMainMenu = () => {
        setOpenedMenu("Main menu")
    }

    let body = <>
        <Header titleOnClick={openMainMenu} buysOnClick={openBuys}/>
    </>

    if (openedMenu === "Main menu") {
        body = <>{body}
            <div className="container pt-0 px-0" id="main">
                <MainMenu buysOnClick={openBuys}/>
            </div>
        </>
    } else if (openedMenu === "Buys") {
        body = <>{body}
            <div className="container pt-0 px-0" id="main">
                <Buys />
            </div>
        </>
    }
    return <>{body}</>
}

const root = createRoot(document.getElementById('app'))
root.render(<App/>)