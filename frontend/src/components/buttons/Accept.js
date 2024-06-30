import accept from "./svg/accept.svg"

const Accept = ({width, height, onClick}) => {
    return (
        <div className="svg-button clickable" onClick={onClick}>
            <img src={accept} alt={""} width={width} height={height} draggable="false"/>
        </div>
    )
}

export default Accept