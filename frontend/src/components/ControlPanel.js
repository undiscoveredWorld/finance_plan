import Button from "./Button";

const ControlPanel = (
    {
        mode = "default",
        editOnClick = () => {},
        cancelOnClick = () => {}
    }) => {
    let message = <></>
    if (mode === "edit" || mode === "delete") {
        message = <h2>Select the row</h2>
    }


    return <div className="buys-table d-flex flex-nowrap w-100 my-4">
        <div className="col w-100"></div>
        {message}
        <EditButton mode={mode} editOnClick={editOnClick}/>
        <Button name="Delete"/>
        <CancelButton mode={mode} cancelOnClick={cancelOnClick}/>
    </div>
}

const EditButton = (
    {
        mode = "default",
        editOnClick = () => {}
    }) => {
    let editButton = <></>

    if (mode === "default") {
        editButton = <Button name="Edit" onClick={editOnClick}/>
    } else if (mode === "edit") {
        editButton = <Button name="Save" onClick={editOnClick}/>
    }

    return editButton
}

const CancelButton = (
    {
        mode = "default",
        cancelOnClick = () => {}
    }) => {
    let cancelButton

    if (mode === "default") {
        cancelButton = <Button name="Cancel" enabled={false}/>
    } else {
        cancelButton = <Button name="Cancel" enabled={true} onClick={cancelOnClick}/>
    }

    return cancelButton
}

export default ControlPanel