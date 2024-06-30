import Button from "./Button";
import {get_value_or_default, empty_func} from "../utils";

const DefaultControlPanel = (props) => {
    const editOnClick = get_value_or_default(props.editOnClick, empty_func)

    return (
        <div className="buys-table-control-panel d-flex flex-nowrap w-100 my-4">
            <div className="col w-100"></div>
            <Button name="Edit" onClick={editOnClick}/>
            <Button name="Delete"/>
        </div>
    )
}

const SubmitControlPanel = (props) => {
    const cancelOnClick = get_value_or_default(props.cancelOnClick, empty_func)

    return (
        <div className="buys-table-control-panel d-flex flex-nowrap w-100 my-4">
            <div className="col w-100"></div>
            <h2>Select row</h2>
            <Button name="Save"/>
            <Button name="Cancel" onClick={cancelOnClick}/>
        </div>
    )
}

class ControlPanelManager {
    constructor(mode, setterMode) {
        this.mode = mode
        this.setterMode = (new_mode) => {
            setterMode(new_mode)
            this.mode = new_mode
        }

        this.editOnClick = () => {
            this.setterMode("edit")
        }
        this.cancelOnClick = () => {
            this.setterMode("default")
        }
    }

    get controlPanel() {
        if (this.mode === "default") return <DefaultControlPanel editOnClick={this.editOnClick}/>
        else if (this.mode === "edit") return <SubmitControlPanel cancelOnClick={this.cancelOnClick}/>
    }
}

export default ControlPanelManager