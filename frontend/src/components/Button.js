const Button = (
    {
        enabled= true,
        name = "",
        onClick = () => {}
    }) => {
    if (enabled)
        return <button className="clickable" type="button" onClick={onClick}><h3>{name}</h3></button>
    else
        return <button disabled className="clickable" type="button"><h3>{name}</h3></button>
}

export default Button