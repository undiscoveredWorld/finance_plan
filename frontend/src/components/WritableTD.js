const WritableTD = ({default_value, setter}) => {
    return <td>
        <input type="text"
               value={default_value}
               onChange={
                   (e) => {
                       setter(e.target.value)
                   }
               }/>
    </td>
}

export default WritableTD