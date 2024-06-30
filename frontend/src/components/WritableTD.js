const WritableTD = (props) => {
    const default_value = props.default_value
    const setter = props.setter

    const input_on_change = (e) => {
        setter(e.target.value)
    }

    return (
        <td>
            <input type="text" value={default_value} onChange={input_on_change}/>
        </td>
    )
}

export default WritableTD