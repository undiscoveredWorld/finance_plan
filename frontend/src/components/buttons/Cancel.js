import cancel from "./svg/cancel.svg"

const Cancel = ({width, height, onClick}) => {
    return (
        <div className="svg-button clickable" onClick={onClick}>
            <img src={cancel} alt={""} width={width} height={height} draggable="false"/>
        </div>
    )
}

export default Cancel
