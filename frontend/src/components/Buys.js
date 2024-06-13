import {useState} from "react";
import ControlPanel from "./ControlPanel";
import Table from "./Table";

const Buys = ({rows}) => {
    const [mode, setMode] = useState("default")
    const editMode = () => {
        setMode("edit")
    }
    const defaultMode = () => {
        setMode("default")
    }

    return <>
        <ControlPanel mode={mode} cancelOnClick={defaultMode} editOnClick={editMode}/>
        <Table rows={rows}/>
    </>
}

export default Buys
