import {useState, useEffect} from "react";
import ControlPanelManager from "./ControlPanel";
import Table from "./Table";
import {is_array_equal_array, get_and_refresh_rows} from "../utils"

const Buys = () => {
    const [mode, setMode] = useState("default")
    const [rows, setRows] = useState([])
    const [selectedRows, setSelectedRows] = useState([])

    const setterMode = (new_mode) => {
        if (new_mode === "default")
            setSelectedRows([])
        setMode(new_mode)
    }
    const refreshRows = (new_rows) => {
        if (!Array.isArray(new_rows)) return undefined
        if (is_array_equal_array(new_rows, rows)) return undefined
        setRows(new_rows)
    }

    useEffect(() => {
        const interval = setInterval(() => {
            get_and_refresh_rows(refreshRows)
        }, 30_000)
        return () => {
            clearInterval(interval)
        }
    },[]);

    useEffect(() => {
        get_and_refresh_rows(refreshRows)
    }, []);

    const control_panel_manager = new ControlPanelManager(mode, setterMode)

    return <>
        {control_panel_manager.controlPanel}
        <div className="container m-0 p-0">
            <Table mode={mode} rows={rows} selectedRows={selectedRows} setSelectedRows={setSelectedRows}/>
        </div>
    </>
}

export default Buys

