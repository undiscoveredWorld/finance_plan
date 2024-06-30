import delete_svg from "./svg/delete.svg"

const Cancel = ({width, height, onClick}) => {
    return <div className="svg-button clickable" onClick={onClick}>
        <img src={delete_svg} alt={""} width={width} height={height} draggable="false"/>
    </div>
}

export default Cancel
