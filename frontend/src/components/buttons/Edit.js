import edit from "./svg/edit.svg"

const Cancel = ({width, height, onClick}) => {
    return <div className="svg-button clickable" onClick={onClick}>
        <img src={edit} alt={""} width={width} height={height} draggable="false"/>
    </div>
}

export default Cancel
