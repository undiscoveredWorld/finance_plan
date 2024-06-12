const Button = ({enabled= true, name = ""}) => {
    if (enabled)
        return <button type="button"><h3>{name}</h3></button>
    else
        return <button disabled type="button"><h3>{name}</h3></button>
}

export default Button