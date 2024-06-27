import { useEffect, useRef, useState } from "react"
import axios from 'axios'

const Categories = () => {

    const [categoria1, setCategoria1] = useState()
    const [subcategoria1, setSubcategoria1] = useState()
    const [subcategoria2, setSubcategoria2] = useState()

    const [categoria2, setCategoria2] = useState()
    const [subcategoria3, setSubcategoria3] = useState()
    const [subcategoria4, setSubcategoria4] = useState()


    useEffect(() => {
        axios
            .get('http://31.128.37.252:8080/categories')
            .then(data =>{
                setSubcategoria3(data.data[1].subcategories[0].name)
                setSubcategoria4(data.data[1].subcategories[1].name)
                setCategoria1(data.data[0].name)
                setCategoria2(data.data[1].name)
                setSubcategoria1(data.data[0].subcategories[0].name)
                setSubcategoria2(data.data[0].subcategories[1].name)
            })
    }, [])

    const createMenuRef = useRef(null)
    const buttonCreateRef = useRef(null)

    const onCreateClick = () => {
        if(!createMenuRef.current) return
        createMenuRef.current.style.display = 'block'
        buttonCreateRef.current.style.display = 'none'
    }

    const DefaultCreate = () => {
        if(!createMenuRef.current && !buttonCreateRef.current) return
        createMenuRef.current.style.display = 'none'
        buttonCreateRef.current.style.display = 'block'
    }

    const createSubcategory1MenuRef = useRef(null)
    const createSubcategory3MenuRef = useRef(null)

    const buttonCreateSubcategory1 = useRef(null)
    const buttonCreateSubcategory3 = useRef(null)


    const DefaultCreateSubcategory1 = () => {
        if(!createSubcategory1MenuRef.current && !buttonCreateSubcategory1.current) return
        createSubcategory1MenuRef.current.style.display = 'none'
        buttonCreateSubcategory1.current.style.display = 'block'
    }

    const DefaultCreateSubcategory3 = () => {
        if(!createSubcategory3MenuRef.current && !buttonCreateSubcategory3.current) return
        createSubcategory3MenuRef.current.style.display = 'none'
        buttonCreateSubcategory3.current.style.display = 'block'
    }


    const OnCreateSubcategory1Click = () => {
        if(!createSubcategory1MenuRef.current) return
        createSubcategory1MenuRef.current.style.display = 'block'
        buttonCreateSubcategory1.current.style.display = 'none'
    }

    const OnCreateSubcategory3Click = () => {
        if(!createSubcategory3MenuRef.current) return
        createSubcategory3MenuRef.current.style.display = 'block'
        buttonCreateSubcategory3.current.style.display = 'none'
    }

    const editingMenuSubcategory1 = useRef(null)
    const editingMenuCreateInputSubcategory1 = useRef(null)
    const subcategory1Standart = useRef(null)
    const deleteMenuSubcategory1 = useRef(null)

    const DefaultSubcategory1 = () => {
        if(!editingMenuCreateInputSubcategory1.current) return
        editingMenuCreateInputSubcategory1.current.style.display = 'none'
        subcategory1Standart.current.style.display = 'block'
    }

    const ChangeInputSubcategory1 = () => {
        if(!editingMenuSubcategory1.current) return
        editingMenuSubcategory1.current.style.display = 'block'
        subcategory1Standart.current.style.display = 'none'
    }

    const EditSubcategory1 = () => {
        if(!editingMenuCreateInputSubcategory1.current) return
        editingMenuCreateInputSubcategory1.current.style.display = 'block'
        editingMenuSubcategory1.current.style.display = 'none'
    }

    const CreateDeleteMenuSubcategory1 = () => {
        if(!deleteMenuSubcategory1.current) return
        deleteMenuSubcategory1.current.style.display = 'block'
        editingMenuSubcategory1.current.style.display = 'none'
    }

    const CloseDeleteMenuSubcategory1 = () => {
        if(!deleteMenuSubcategory1.current) return
        deleteMenuSubcategory1.current.style.display = 'none'
        subcategory1Standart.current.style.display = 'block'
    }

    const editingMenuSubcategory2 = useRef(null)
    const editingMenuCreateInputSubcategory2 = useRef(null)
    const subcategory2Standart = useRef(null)
    const deleteMenuSubcategory2 = useRef(null)

    const DefaultSubcategory2 = () => {
        if(!editingMenuCreateInputSubcategory2.current) return
        editingMenuCreateInputSubcategory2.current.style.display = 'none'
        subcategory2Standart.current.style.display = 'block'
    }

    const ChangeInputSubcategory2 = () => {
        if(!editingMenuSubcategory2.current) return
        editingMenuSubcategory2.current.style.display = 'block'
        subcategory2Standart.current.style.display = 'none'
    }

    const EditSubcategory2 = () => {
        if(!editingMenuCreateInputSubcategory2.current) return
        editingMenuCreateInputSubcategory2.current.style.display = 'block'
        editingMenuSubcategory2.current.style.display = 'none'
    }

    const CreateDeleteMenuSubcategory2 = () => {
        if(!deleteMenuSubcategory2.current) return
        deleteMenuSubcategory2.current.style.display = 'block'
        editingMenuSubcategory2.current.style.display = 'none'
    }

    const CloseDeleteMenuSubcategory2 = () => {
        if(!deleteMenuSubcategory2.current) return
        deleteMenuSubcategory2.current.style.display = 'none'
        subcategory2Standart.current.style.display = 'block'
    }


    const editingMenuSubcategory3 = useRef(null)
    const editingMenuCreateInputSubcategory3 = useRef(null)
    const subcategory3Standart = useRef(null)
    const deleteMenuSubcategory3 = useRef(null)

    const DefaultSubcategory3 = () => {
        if(!editingMenuCreateInputSubcategory3.current) return
        editingMenuCreateInputSubcategory3.current.style.display = 'none'
        subcategory3Standart.current.style.display = 'block'
    }

    const ChangeInputSubcategory3 = () => {
        if(!editingMenuSubcategory3.current) return
        editingMenuSubcategory3.current.style.display = 'block'
        subcategory3Standart.current.style.display = 'none'
    }

    const EditSubcategory3 = () => {
        if(!editingMenuCreateInputSubcategory3.current) return
        editingMenuCreateInputSubcategory3.current.style.display = 'block'
        editingMenuSubcategory3.current.style.display = 'none'
    }

    const CreateDeleteMenuSubcategory3 = () => {
        if(!deleteMenuSubcategory3.current) return
        deleteMenuSubcategory3.current.style.display = 'block'
        editingMenuSubcategory3.current.style.display = 'none'
    }

    const CloseDeleteMenuSubcategory3 = () => {
        if(!deleteMenuSubcategory3.current) return
        deleteMenuSubcategory3.current.style.display = 'none'
        subcategory3Standart.current.style.display = 'block'
    }


    const editingMenuSubcategory4 = useRef(null)
    const editingMenuCreateInputSubcategory4 = useRef(null)
    const subcategory4Standart = useRef(null)
    const deleteMenuSubcategory4 = useRef(null)

    const DefaultSubcategory4 = () => {
        if(!editingMenuCreateInputSubcategory4.current) return
        editingMenuCreateInputSubcategory4.current.style.display = 'none'
        subcategory4Standart.current.style.display = 'block'
    }

    const ChangeInputSubcategory4 = () => {
        if(!editingMenuSubcategory4.current) return
        editingMenuSubcategory4.current.style.display = 'block'
        subcategory4Standart.current.style.display = 'none'
    }

    const EditSubcategory4 = () => {
        if(!editingMenuCreateInputSubcategory4.current) return
        editingMenuCreateInputSubcategory4.current.style.display = 'block'
        editingMenuSubcategory4.current.style.display = 'none'
    }

    const CreateDeleteMenuSubcategory4 = () => {
        if(!deleteMenuSubcategory4.current) return
        deleteMenuSubcategory4.current.style.display = 'block'
        editingMenuSubcategory4.current.style.display = 'none'
    }

    const CloseDeleteMenuSubcategory4 = () => {
        if(!deleteMenuSubcategory4.current) return
        deleteMenuSubcategory4.current.style.display = 'none'
        subcategory4Standart.current.style.display = 'block'
    }


    const editingMenuСategory1 = useRef(null)
    const editingMenuCreateInputСategory1 = useRef(null)
    const category1Standart = useRef(null)
    const deleteMenuСategory1 = useRef(null)

    const DefaultСategory1= () => {
        if(!editingMenuCreateInputСategory1.current) return
        editingMenuCreateInputСategory1.current.style.display = 'none'
        category1Standart.current.style.display = 'block'
    }

    const ChangeInputСategory1 = () => {
        if(!editingMenuСategory1.current) return
        editingMenuСategory1.current.style.display = 'block'
        category1Standart.current.style.display = 'none'
    }

    const EditСategory1 = () => {
        if(!editingMenuCreateInputСategory1.current) return
        editingMenuCreateInputСategory1.current.style.display = 'block'
        editingMenuСategory1.current.style.display = 'none'
    }

    const CreateDeleteMenuСategory1 = () => {
        if(!deleteMenuСategory1.current) return
        deleteMenuСategory1.current.style.display = 'block'
        editingMenuСategory1.current.style.display = 'none'
    }

    const CloseDeleteMenuСategory1= () => {
        if(!deleteMenuСategory1.current) return
        deleteMenuСategory1.current.style.display = 'none'
        category1Standart.current.style.display = 'block'
    }

    const editingMenuСategory2 = useRef(null)
    const editingMenuCreateInputСategory2 = useRef(null)
    const category2Standart = useRef(null)
    const deleteMenuСategory2 = useRef(null)

    const DefaultСategory2 = () => {
        if(!editingMenuCreateInputСategory2.current) return
        editingMenuCreateInputСategory2.current.style.display = 'none'
        category2Standart.current.style.display = 'block'
    }

    const ChangeInputСategory2 = () => {
        if(!editingMenuСategory2.current) return
        editingMenuСategory2.current.style.display = 'block'
        category2Standart.current.style.display = 'none'
    }

    const EditСategory2 = () => {
        if(!editingMenuCreateInputСategory2.current) return
        editingMenuCreateInputСategory2.current.style.display = 'block'
        editingMenuСategory2.current.style.display = 'none'
    }

    const CreateDeleteMenuСategory2 = () => {
        if(!deleteMenuСategory2.current) return
        deleteMenuСategory2.current.style.display = 'block'
        editingMenuСategory2.current.style.display = 'none'
    }

    const CloseDeleteMenuСategory2 = () => {
        if(!deleteMenuСategory2.current) return
        deleteMenuСategory2.current.style.display = 'none'
        category2Standart.current.style.display = 'block'
    }

    return <>
        <div className="menu">
            <button className="create_button" onClick={onCreateClick} ref={buttonCreateRef}><h1>Create</h1></button>
            <div className="create_input_container" ref={createMenuRef}>
                <input className="input"/>
                <button className="change_button">
                    <svg width="82.1px" height="57.76px" viewBox="0 0 20 20" version="1.1" xmlns="http://www.w3.org/2000/svg">
                        <g id="layer1">
                            <path d="M 18.837891 3.2832031 L 6.8183594 15.302734 L 1.1621094 9.6464844 L 0.453125 10.353516 L 6.8183594 16.716797 L 19.546875 3.9902344 L 18.837891 3.2832031 z " />
                        </g>
                    </svg>
                </button>
                <button className="change_button" onClick={DefaultCreate}>
                    <svg width="55.26px" height="55.26px" viewBox="0 0 512 512" version="1.1" xmlns="http://www.w3.org/2000/svg">
                        <title>cancel</title>
                        <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                            <g id="work-case" fill="#000000" transform="translate(91.520000, 91.520000)">
                                <polygon id="Close" points="328.96 30.2933333 298.666667 1.42108547e-14 164.48 134.4 30.2933333 1.42108547e-14 1.42108547e-14 30.2933333 134.4 164.48 1.42108547e-14 298.666667 30.2933333 328.96 164.48 194.56 298.666667 328.96 328.96 298.666667 194.56 164.48">
                                </polygon>
                            </g>
                        </g>
                    </svg>
                </button>
            </div>

            {(<button className="default_button" onClick={ChangeInputСategory1} ref={category1Standart}><h1>{categoria1}</h1></button>)}

            <div ref={editingMenuСategory1} className="editing_menu">
                <button className="editing_button"><h1>{categoria1}</h1></button>
                <button className="change_button" onClick={EditСategory1}>
                    <svg width="60.97px" height="60.97px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd" clip-rule="evenodd" d="M14.2322 5.76777C15.2085 4.79146 16.7915 4.79146 17.7678 5.76777L18.4749 6.47487C19.4512 7.45118 19.4512 9.0341 18.4749 10.0104L10.3431 18.1421L7.10051 18.1421C6.54822 18.1421 6.1005 17.6944 6.10051 17.1421L6.10051 13.8995L14.2322 5.76777ZM16.3536 7.18198L17.0607 7.88909C17.2559 8.08435 17.2559 8.40093 17.0607 8.59619L16 9.65685L14.5858 8.24264L15.6464 7.18198C15.8417 6.98672 16.1583 6.98672 16.3536 7.18198ZM14.5858 11.0711L9.51472 16.1421L8.10051 16.1421L8.10051 14.7279L13.1716 9.65685L14.5858 11.0711Z" fill="#000000"/>
                    </svg>
                </button>
                <button className="change_button" onClick={CreateDeleteMenuСategory1}>
                    <svg width="86px" height="81.9px" viewBox="0 -0.5 21 21" version="1.1" xmlns="http://www.w3.org/2000/svg">
                        <title>delete [#1487]</title>
                        <desc>Created with Sketch.</desc>
                        <defs>
                        </defs>
                        <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                            <g id="Dribbble-Light-Preview" transform="translate(-179.000000, -360.000000)" fill="#000000">
                                <g id="icons" transform="translate(56.000000, 160.000000)">
                                    <path d="M130.35,216 L132.45,216 L132.45,208 L130.35,208 L130.35,216 Z M134.55,216 L136.65,216 L136.65,208 L134.55,208 L134.55,216 Z M128.25,218 L138.75,218 L138.75,206 L128.25,206 L128.25,218 Z M130.35,204 L136.65,204 L136.65,202 L130.35,202 L130.35,204 Z M138.75,204 L138.75,200 L128.25,200 L128.25,204 L123,204 L123,206 L126.15,206 L126.15,220 L140.85,220 L140.85,206 L144,206 L144,204 L138.75,204 Z" id="delete-[#1487]">
                                    </path>
                                </g>
                            </g>
                        </g>
                    </svg>
                </button>
            </div>
            <div className="delete_menu_container" ref={deleteMenuСategory1}>
                <button className="delete_button_default"><h1>{categoria1}</h1></button>
                <button className="change_button_delete">
                    <svg width="82.1px" height="57.76px" viewBox="0 0 20 20" version="1.1" xmlns="http://www.w3.org/2000/svg">
                        <g id="layer1">
                            <path d="M 18.837891 3.2832031 L 6.8183594 15.302734 L 1.1621094 9.6464844 L 0.453125 10.353516 L 6.8183594 16.716797 L 19.546875 3.9902344 L 18.837891 3.2832031 z " />
                        </g>
                    </svg>
                </button>
                <button className="change_button_delete" onClick={CloseDeleteMenuСategory1}>
                    <svg width="55.26px" height="55.26px" viewBox="0 0 512 512" version="1.1" xmlns="http://www.w3.org/2000/svg">
                        <title>cancel</title>
                        <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                            <g id="work-case" fill="#000000" transform="translate(91.520000, 91.520000)">
                                <polygon id="Close" points="328.96 30.2933333 298.666667 1.42108547e-14 164.48 134.4 30.2933333 1.42108547e-14 1.42108547e-14 30.2933333 134.4 164.48 1.42108547e-14 298.666667 30.2933333 328.96 164.48 194.56 298.666667 328.96 328.96 298.666667 194.56 164.48">
                                </polygon>
                            </g>
                        </g>
                    </svg>
                </button>
            </div>
            <div className="input_menu_container" ref={editingMenuCreateInputСategory1}>
                <input className="input"/>
                <button className="change_button">
                    <svg width="82.1px" height="57.76px" viewBox="0 0 20 20" version="1.1" xmlns="http://www.w3.org/2000/svg">
                        <g id="layer1">
                            <path d="M 18.837891 3.2832031 L 6.8183594 15.302734 L 1.1621094 9.6464844 L 0.453125 10.353516 L 6.8183594 16.716797 L 19.546875 3.9902344 L 18.837891 3.2832031 z " />
                        </g>
                    </svg>
                </button>
                <button className="change_button" onClick={DefaultСategory1}>
                    <svg width="55.26px" height="55.26px" viewBox="0 0 512 512" version="1.1" xmlns="http://www.w3.org/2000/svg">
                        <title>cancel</title>
                        <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                            <g id="work-case" fill="#000000" transform="translate(91.520000, 91.520000)">
                                <polygon id="Close" points="328.96 30.2933333 298.666667 1.42108547e-14 164.48 134.4 30.2933333 1.42108547e-14 1.42108547e-14 30.2933333 134.4 164.48 1.42108547e-14 298.666667 30.2933333 328.96 164.48 194.56 298.666667 328.96 328.96 298.666667 194.56 164.48">
                                </polygon>
                            </g>
                        </g>
                    </svg>
                </button>
            </div>


            <button className="subcategory_create" onClick={OnCreateSubcategory1Click} ref={buttonCreateSubcategory1}><h1>Create</h1></button>
            <div className="subcategory_create_input_container" ref={createSubcategory1MenuRef}>
                <input className="input_subcategories"/>
                <button className="change_button_subcategories_create">
                    <svg width="82.1px" height="57.76px" viewBox="0 0 20 20" version="1.1" xmlns="http://www.w3.org/2000/svg">
                        <g id="layer1">
                            <path d="M 18.837891 3.2832031 L 6.8183594 15.302734 L 1.1621094 9.6464844 L 0.453125 10.353516 L 6.8183594 16.716797 L 19.546875 3.9902344 L 18.837891 3.2832031 z " />
                        </g>
                    </svg>
                </button>
                <button className="change_button_subcategories_create" onClick={DefaultCreateSubcategory1}>
                    <svg width="55.26px" height="55.26px" viewBox="0 0 512 512" version="1.1" xmlns="http://www.w3.org/2000/svg">
                        <title>cancel</title>
                        <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                            <g id="work-case" fill="#000000" transform="translate(91.520000, 91.520000)">
                                <polygon id="Close" points="328.96 30.2933333 298.666667 1.42108547e-14 164.48 134.4 30.2933333 1.42108547e-14 1.42108547e-14 30.2933333 134.4 164.48 1.42108547e-14 298.666667 30.2933333 328.96 164.48 194.56 298.666667 328.96 328.96 298.666667 194.56 164.48">
                                </polygon>
                            </g>
                        </g>
                    </svg>
                </button>
            </div>

            {(<button className="subcategory_button" onClick={ChangeInputSubcategory1} ref={subcategory1Standart}><h1>{subcategoria1}</h1></button>)}

            <div ref={editingMenuSubcategory1} className="editing_menu_subcategories">
                <button className="editing_button_subcategories"><h1>{subcategoria1}</h1></button>
                <button className="change_button_subcategories" onClick={EditSubcategory1}>
                    <svg width="60.97px" height="60.97px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd" clip-rule="evenodd" d="M14.2322 5.76777C15.2085 4.79146 16.7915 4.79146 17.7678 5.76777L18.4749 6.47487C19.4512 7.45118 19.4512 9.0341 18.4749 10.0104L10.3431 18.1421L7.10051 18.1421C6.54822 18.1421 6.1005 17.6944 6.10051 17.1421L6.10051 13.8995L14.2322 5.76777ZM16.3536 7.18198L17.0607 7.88909C17.2559 8.08435 17.2559 8.40093 17.0607 8.59619L16 9.65685L14.5858 8.24264L15.6464 7.18198C15.8417 6.98672 16.1583 6.98672 16.3536 7.18198ZM14.5858 11.0711L9.51472 16.1421L8.10051 16.1421L8.10051 14.7279L13.1716 9.65685L14.5858 11.0711Z" fill="#000000"/>
                    </svg>
                </button>
                <button className="change_button_subcategories" onClick={CreateDeleteMenuSubcategory1}>
                    <svg width="86px" height="81.9px" viewBox="0 -0.5 21 21" version="1.1" xmlns="http://www.w3.org/2000/svg">
                        <title>delete [#1487]</title>
                        <desc>Created with Sketch.</desc>
                        <defs>
                        </defs>
                        <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                            <g id="Dribbble-Light-Preview" transform="translate(-179.000000, -360.000000)" fill="#000000">
                                <g id="icons" transform="translate(56.000000, 160.000000)">
                                    <path d="M130.35,216 L132.45,216 L132.45,208 L130.35,208 L130.35,216 Z M134.55,216 L136.65,216 L136.65,208 L134.55,208 L134.55,216 Z M128.25,218 L138.75,218 L138.75,206 L128.25,206 L128.25,218 Z M130.35,204 L136.65,204 L136.65,202 L130.35,202 L130.35,204 Z M138.75,204 L138.75,200 L128.25,200 L128.25,204 L123,204 L123,206 L126.15,206 L126.15,220 L140.85,220 L140.85,206 L144,206 L144,204 L138.75,204 Z" id="delete-[#1487]">
                                    </path>
                                </g>
                            </g>
                        </g>
                    </svg>
                </button>
            </div>
            <div className="delete_menu_container_subcategories" ref={deleteMenuSubcategory1}>
                <button className="delete_button_default_subcategories"><h1>{subcategoria1}</h1></button>
                <button className="change_button_delete_subcategories">
                    <svg width="82.1px" height="57.76px" viewBox="0 0 20 20" version="1.1" xmlns="http://www.w3.org/2000/svg">
                        <g id="layer1">
                            <path d="M 18.837891 3.2832031 L 6.8183594 15.302734 L 1.1621094 9.6464844 L 0.453125 10.353516 L 6.8183594 16.716797 L 19.546875 3.9902344 L 18.837891 3.2832031 z " />
                        </g>
                    </svg>
                </button>
                <button className="change_button_delete_subcategories" onClick={CloseDeleteMenuSubcategory1}>
                    <svg width="55.26px" height="55.26px" viewBox="0 0 512 512" version="1.1" xmlns="http://www.w3.org/2000/svg">
                        <title>cancel</title>
                        <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                            <g id="work-case" fill="#000000" transform="translate(91.520000, 91.520000)">
                                <polygon id="Close" points="328.96 30.2933333 298.666667 1.42108547e-14 164.48 134.4 30.2933333 1.42108547e-14 1.42108547e-14 30.2933333 134.4 164.48 1.42108547e-14 298.666667 30.2933333 328.96 164.48 194.56 298.666667 328.96 328.96 298.666667 194.56 164.48">
                                </polygon>
                            </g>
                        </g>
                    </svg>
                </button>
            </div>
            <div className="subcategories_input_container" ref={editingMenuCreateInputSubcategory1}>
                <input className="input_subcategories"/>
                <button className="change_button_subcategories_create">
                    <svg width="82.1px" height="57.76px" viewBox="0 0 20 20" version="1.1" xmlns="http://www.w3.org/2000/svg">
                        <g id="layer1">
                            <path d="M 18.837891 3.2832031 L 6.8183594 15.302734 L 1.1621094 9.6464844 L 0.453125 10.353516 L 6.8183594 16.716797 L 19.546875 3.9902344 L 18.837891 3.2832031 z " />
                        </g>
                    </svg>
                </button>
                <button className="change_button_subcategories_create" onClick={DefaultSubcategory1}>
                    <svg width="55.26px" height="55.26px" viewBox="0 0 512 512" version="1.1" xmlns="http://www.w3.org/2000/svg">
                        <title>cancel</title>
                        <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                            <g id="work-case" fill="#000000" transform="translate(91.520000, 91.520000)">
                                <polygon id="Close" points="328.96 30.2933333 298.666667 1.42108547e-14 164.48 134.4 30.2933333 1.42108547e-14 1.42108547e-14 30.2933333 134.4 164.48 1.42108547e-14 298.666667 30.2933333 328.96 164.48 194.56 298.666667 328.96 328.96 298.666667 194.56 164.48">
                                </polygon>
                            </g>
                        </g>
                    </svg>
                </button>
            </div>

            {(<button className="subcategory_button" onClick={ChangeInputSubcategory2} ref={subcategory2Standart}><h1>{subcategoria2}</h1></button>)}

            <div ref={editingMenuSubcategory2} className="editing_menu_subcategories">
                <button className="editing_button_subcategories"><h1>{subcategoria2}</h1></button>
                <button className="change_button_subcategories" onClick={EditSubcategory2}>
                    <svg width="60.97px" height="60.97px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd" clip-rule="evenodd" d="M14.2322 5.76777C15.2085 4.79146 16.7915 4.79146 17.7678 5.76777L18.4749 6.47487C19.4512 7.45118 19.4512 9.0341 18.4749 10.0104L10.3431 18.1421L7.10051 18.1421C6.54822 18.1421 6.1005 17.6944 6.10051 17.1421L6.10051 13.8995L14.2322 5.76777ZM16.3536 7.18198L17.0607 7.88909C17.2559 8.08435 17.2559 8.40093 17.0607 8.59619L16 9.65685L14.5858 8.24264L15.6464 7.18198C15.8417 6.98672 16.1583 6.98672 16.3536 7.18198ZM14.5858 11.0711L9.51472 16.1421L8.10051 16.1421L8.10051 14.7279L13.1716 9.65685L14.5858 11.0711Z" fill="#000000"/>
                    </svg>
                </button>
                <button className="change_button_subcategories" onClick={CreateDeleteMenuSubcategory2}>
                    <svg width="86px" height="81.9px" viewBox="0 -0.5 21 21" version="1.1" xmlns="http://www.w3.org/2000/svg">
                        <title>delete [#1487]</title>
                        <desc>Created with Sketch.</desc>
                        <defs>
                        </defs>
                        <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                            <g id="Dribbble-Light-Preview" transform="translate(-179.000000, -360.000000)" fill="#000000">
                                <g id="icons" transform="translate(56.000000, 160.000000)">
                                    <path d="M130.35,216 L132.45,216 L132.45,208 L130.35,208 L130.35,216 Z M134.55,216 L136.65,216 L136.65,208 L134.55,208 L134.55,216 Z M128.25,218 L138.75,218 L138.75,206 L128.25,206 L128.25,218 Z M130.35,204 L136.65,204 L136.65,202 L130.35,202 L130.35,204 Z M138.75,204 L138.75,200 L128.25,200 L128.25,204 L123,204 L123,206 L126.15,206 L126.15,220 L140.85,220 L140.85,206 L144,206 L144,204 L138.75,204 Z" id="delete-[#1487]">
                                    </path>
                                </g>
                            </g>
                        </g>
                    </svg>
                </button>
            </div>
            <div className="delete_menu_container_subcategories" ref={deleteMenuSubcategory2}>
                <button className="delete_button_default_subcategories"><h1>{subcategoria2}</h1></button>
                <button className="change_button_delete_subcategories">
                    <svg width="82.1px" height="57.76px" viewBox="0 0 20 20" version="1.1" xmlns="http://www.w3.org/2000/svg">
                        <g id="layer1">
                            <path d="M 18.837891 3.2832031 L 6.8183594 15.302734 L 1.1621094 9.6464844 L 0.453125 10.353516 L 6.8183594 16.716797 L 19.546875 3.9902344 L 18.837891 3.2832031 z " />
                        </g>
                    </svg>
                </button>
                <button className="change_button_delete_subcategories" onClick={CloseDeleteMenuSubcategory2}>
                    <svg width="55.26px" height="55.26px" viewBox="0 0 512 512" version="1.1" xmlns="http://www.w3.org/2000/svg">
                        <title>cancel</title>
                        <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                            <g id="work-case" fill="#000000" transform="translate(91.520000, 91.520000)">
                                <polygon id="Close" points="328.96 30.2933333 298.666667 1.42108547e-14 164.48 134.4 30.2933333 1.42108547e-14 1.42108547e-14 30.2933333 134.4 164.48 1.42108547e-14 298.666667 30.2933333 328.96 164.48 194.56 298.666667 328.96 328.96 298.666667 194.56 164.48">
                                </polygon>
                            </g>
                        </g>
                    </svg>
                </button>
            </div>
            <div className="subcategories_input_container" ref={editingMenuCreateInputSubcategory2}>
                <input className="input_subcategories"/>
                <button className="change_button_subcategories_create">
                    <svg width="82.1px" height="57.76px" viewBox="0 0 20 20" version="1.1" xmlns="http://www.w3.org/2000/svg">
                        <g id="layer1">
                            <path d="M 18.837891 3.2832031 L 6.8183594 15.302734 L 1.1621094 9.6464844 L 0.453125 10.353516 L 6.8183594 16.716797 L 19.546875 3.9902344 L 18.837891 3.2832031 z " />
                        </g>
                    </svg>
                </button>
                <button className="change_button_subcategories_create" onClick={DefaultSubcategory2}>
                    <svg width="55.26px" height="55.26px" viewBox="0 0 512 512" version="1.1" xmlns="http://www.w3.org/2000/svg">
                        <title>cancel</title>
                        <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                            <g id="work-case" fill="#000000" transform="translate(91.520000, 91.520000)">
                                <polygon id="Close" points="328.96 30.2933333 298.666667 1.42108547e-14 164.48 134.4 30.2933333 1.42108547e-14 1.42108547e-14 30.2933333 134.4 164.48 1.42108547e-14 298.666667 30.2933333 328.96 164.48 194.56 298.666667 328.96 328.96 298.666667 194.56 164.48">
                                </polygon>
                            </g>
                        </g>
                    </svg>
                </button>
            </div>

            {(<button className="default_button" onClick={ChangeInputСategory2} ref={category2Standart}><h1>{categoria2}</h1></button>)}

            <div ref={editingMenuСategory2} className="editing_menu">
                <button className="editing_button"><h1>{categoria2}</h1></button>
                <button className="change_button" onClick={EditСategory2}>
                    <svg width="60.97px" height="60.97px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd" clip-rule="evenodd" d="M14.2322 5.76777C15.2085 4.79146 16.7915 4.79146 17.7678 5.76777L18.4749 6.47487C19.4512 7.45118 19.4512 9.0341 18.4749 10.0104L10.3431 18.1421L7.10051 18.1421C6.54822 18.1421 6.1005 17.6944 6.10051 17.1421L6.10051 13.8995L14.2322 5.76777ZM16.3536 7.18198L17.0607 7.88909C17.2559 8.08435 17.2559 8.40093 17.0607 8.59619L16 9.65685L14.5858 8.24264L15.6464 7.18198C15.8417 6.98672 16.1583 6.98672 16.3536 7.18198ZM14.5858 11.0711L9.51472 16.1421L8.10051 16.1421L8.10051 14.7279L13.1716 9.65685L14.5858 11.0711Z" fill="#000000"/>
                    </svg>
                </button>
                <button className="change_button" onClick={CreateDeleteMenuСategory2}>
                    <svg width="86px" height="81.9px" viewBox="0 -0.5 21 21" version="1.1" xmlns="http://www.w3.org/2000/svg">
                        <title>delete [#1487]</title>
                        <desc>Created with Sketch.</desc>
                        <defs>
                        </defs>
                        <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                            <g id="Dribbble-Light-Preview" transform="translate(-179.000000, -360.000000)" fill="#000000">
                                <g id="icons" transform="translate(56.000000, 160.000000)">
                                    <path d="M130.35,216 L132.45,216 L132.45,208 L130.35,208 L130.35,216 Z M134.55,216 L136.65,216 L136.65,208 L134.55,208 L134.55,216 Z M128.25,218 L138.75,218 L138.75,206 L128.25,206 L128.25,218 Z M130.35,204 L136.65,204 L136.65,202 L130.35,202 L130.35,204 Z M138.75,204 L138.75,200 L128.25,200 L128.25,204 L123,204 L123,206 L126.15,206 L126.15,220 L140.85,220 L140.85,206 L144,206 L144,204 L138.75,204 Z" id="delete-[#1487]">
                                    </path>
                                </g>
                            </g>
                        </g>
                    </svg>
                </button>
            </div>
            <div className="delete_menu_container" ref={deleteMenuСategory2}>
                <button className="delete_button_default"><h1>{categoria2}</h1></button>
                <button className="change_button_delete">
                    <svg width="82.1px" height="57.76px" viewBox="0 0 20 20" version="1.1" xmlns="http://www.w3.org/2000/svg">
                        <g id="layer1">
                            <path d="M 18.837891 3.2832031 L 6.8183594 15.302734 L 1.1621094 9.6464844 L 0.453125 10.353516 L 6.8183594 16.716797 L 19.546875 3.9902344 L 18.837891 3.2832031 z " />
                        </g>
                    </svg>
                </button>
                <button className="change_button_delete" onClick={CloseDeleteMenuСategory2}>
                    <svg width="55.26px" height="55.26px" viewBox="0 0 512 512" version="1.1" xmlns="http://www.w3.org/2000/svg">
                        <title>cancel</title>
                        <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                            <g id="work-case" fill="#000000" transform="translate(91.520000, 91.520000)">
                                <polygon id="Close" points="328.96 30.2933333 298.666667 1.42108547e-14 164.48 134.4 30.2933333 1.42108547e-14 1.42108547e-14 30.2933333 134.4 164.48 1.42108547e-14 298.666667 30.2933333 328.96 164.48 194.56 298.666667 328.96 328.96 298.666667 194.56 164.48">
                                </polygon>
                            </g>
                        </g>
                    </svg>
                </button>
            </div>
            <div className="input_menu_container" ref={editingMenuCreateInputСategory2}>
                <input className="input"/>
                <button className="change_button">
                    <svg width="82.1px" height="57.76px" viewBox="0 0 20 20" version="1.1" xmlns="http://www.w3.org/2000/svg">
                        <g id="layer1">
                            <path d="M 18.837891 3.2832031 L 6.8183594 15.302734 L 1.1621094 9.6464844 L 0.453125 10.353516 L 6.8183594 16.716797 L 19.546875 3.9902344 L 18.837891 3.2832031 z " />
                        </g>
                    </svg>
                </button>
                <button className="change_button" onClick={DefaultСategory2}>
                    <svg width="55.26px" height="55.26px" viewBox="0 0 512 512" version="1.1" xmlns="http://www.w3.org/2000/svg">
                        <title>cancel</title>
                        <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                            <g id="work-case" fill="#000000" transform="translate(91.520000, 91.520000)">
                                <polygon id="Close" points="328.96 30.2933333 298.666667 1.42108547e-14 164.48 134.4 30.2933333 1.42108547e-14 1.42108547e-14 30.2933333 134.4 164.48 1.42108547e-14 298.666667 30.2933333 328.96 164.48 194.56 298.666667 328.96 328.96 298.666667 194.56 164.48">
                                </polygon>
                            </g>
                        </g>
                    </svg>
                </button>
            </div>
            
            <button className="subcategory_create" onClick={OnCreateSubcategory3Click} ref={buttonCreateSubcategory3}><h1>Create</h1></button>
            <div className="subcategory_create_input_container" ref={createSubcategory3MenuRef}>
                <input className="input_subcategories"/>
                <button className="change_button_subcategories_create">
                    <svg width="82.1px" height="57.76px" viewBox="0 0 20 20" version="1.1" xmlns="http://www.w3.org/2000/svg">
                        <g id="layer1">
                            <path d="M 18.837891 3.2832031 L 6.8183594 15.302734 L 1.1621094 9.6464844 L 0.453125 10.353516 L 6.8183594 16.716797 L 19.546875 3.9902344 L 18.837891 3.2832031 z " />
                        </g>
                    </svg>
                </button>
                <button className="change_button_subcategories_create" onClick={DefaultCreateSubcategory3}>
                    <svg width="55.26px" height="55.26px" viewBox="0 0 512 512" version="1.1" xmlns="http://www.w3.org/2000/svg">
                        <title>cancel</title>
                        <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                            <g id="work-case" fill="#000000" transform="translate(91.520000, 91.520000)">
                                <polygon id="Close" points="328.96 30.2933333 298.666667 1.42108547e-14 164.48 134.4 30.2933333 1.42108547e-14 1.42108547e-14 30.2933333 134.4 164.48 1.42108547e-14 298.666667 30.2933333 328.96 164.48 194.56 298.666667 328.96 328.96 298.666667 194.56 164.48">
                                </polygon>
                            </g>
                        </g>
                    </svg>
                </button>
            </div>


            {(<button className="subcategory_button" onClick={ChangeInputSubcategory3} ref={subcategory3Standart}><h1>{subcategoria3}</h1></button>)}

            <div ref={editingMenuSubcategory3} className="editing_menu_subcategories">
                <button className="editing_button_subcategories"><h1>{subcategoria3}</h1></button>
                <button className="change_button_subcategories" onClick={EditSubcategory3}>
                    <svg width="60.97px" height="60.97px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd" clip-rule="evenodd" d="M14.2322 5.76777C15.2085 4.79146 16.7915 4.79146 17.7678 5.76777L18.4749 6.47487C19.4512 7.45118 19.4512 9.0341 18.4749 10.0104L10.3431 18.1421L7.10051 18.1421C6.54822 18.1421 6.1005 17.6944 6.10051 17.1421L6.10051 13.8995L14.2322 5.76777ZM16.3536 7.18198L17.0607 7.88909C17.2559 8.08435 17.2559 8.40093 17.0607 8.59619L16 9.65685L14.5858 8.24264L15.6464 7.18198C15.8417 6.98672 16.1583 6.98672 16.3536 7.18198ZM14.5858 11.0711L9.51472 16.1421L8.10051 16.1421L8.10051 14.7279L13.1716 9.65685L14.5858 11.0711Z" fill="#000000"/>
                    </svg>
                </button>
                <button className="change_button_subcategories" onClick={CreateDeleteMenuSubcategory3}>
                    <svg width="86px" height="81.9px" viewBox="0 -0.5 21 21" version="1.1" xmlns="http://www.w3.org/2000/svg">
                        <title>delete [#1487]</title>
                        <desc>Created with Sketch.</desc>
                        <defs>
                        </defs>
                        <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                            <g id="Dribbble-Light-Preview" transform="translate(-179.000000, -360.000000)" fill="#000000">
                                <g id="icons" transform="translate(56.000000, 160.000000)">
                                    <path d="M130.35,216 L132.45,216 L132.45,208 L130.35,208 L130.35,216 Z M134.55,216 L136.65,216 L136.65,208 L134.55,208 L134.55,216 Z M128.25,218 L138.75,218 L138.75,206 L128.25,206 L128.25,218 Z M130.35,204 L136.65,204 L136.65,202 L130.35,202 L130.35,204 Z M138.75,204 L138.75,200 L128.25,200 L128.25,204 L123,204 L123,206 L126.15,206 L126.15,220 L140.85,220 L140.85,206 L144,206 L144,204 L138.75,204 Z" id="delete-[#1487]">
                                    </path>
                                </g>
                            </g>
                        </g>
                    </svg>
                </button>
            </div>
            <div className="delete_menu_container_subcategories" ref={deleteMenuSubcategory3}>
                <button className="delete_button_default_subcategories"><h1>{subcategoria3}</h1></button>
                <button className="change_button_delete_subcategories">
                    <svg width="82.1px" height="57.76px" viewBox="0 0 20 20" version="1.1" xmlns="http://www.w3.org/2000/svg">
                        <g id="layer1">
                            <path d="M 18.837891 3.2832031 L 6.8183594 15.302734 L 1.1621094 9.6464844 L 0.453125 10.353516 L 6.8183594 16.716797 L 19.546875 3.9902344 L 18.837891 3.2832031 z " />
                        </g>
                    </svg>
                </button>
                <button className="change_button_delete_subcategories" onClick={CloseDeleteMenuSubcategory3}>
                    <svg width="55.26px" height="55.26px" viewBox="0 0 512 512" version="1.1" xmlns="http://www.w3.org/2000/svg">
                        <title>cancel</title>
                        <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                            <g id="work-case" fill="#000000" transform="translate(91.520000, 91.520000)">
                                <polygon id="Close" points="328.96 30.2933333 298.666667 1.42108547e-14 164.48 134.4 30.2933333 1.42108547e-14 1.42108547e-14 30.2933333 134.4 164.48 1.42108547e-14 298.666667 30.2933333 328.96 164.48 194.56 298.666667 328.96 328.96 298.666667 194.56 164.48">
                                </polygon>
                            </g>
                        </g>
                    </svg>
                </button>
            </div>
            <div className="subcategories_input_container" ref={editingMenuCreateInputSubcategory3}>
                <input className="input_subcategories"/>
                <button className="change_button_subcategories_create">
                    <svg width="82.1px" height="57.76px" viewBox="0 0 20 20" version="1.1" xmlns="http://www.w3.org/2000/svg">
                        <g id="layer1">
                            <path d="M 18.837891 3.2832031 L 6.8183594 15.302734 L 1.1621094 9.6464844 L 0.453125 10.353516 L 6.8183594 16.716797 L 19.546875 3.9902344 L 18.837891 3.2832031 z " />
                        </g>
                    </svg>
                </button>
                <button className="change_button_subcategories_create" onClick={DefaultSubcategory3}>
                    <svg width="55.26px" height="55.26px" viewBox="0 0 512 512" version="1.1" xmlns="http://www.w3.org/2000/svg">
                        <title>cancel</title>
                        <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                            <g id="work-case" fill="#000000" transform="translate(91.520000, 91.520000)">
                                <polygon id="Close" points="328.96 30.2933333 298.666667 1.42108547e-14 164.48 134.4 30.2933333 1.42108547e-14 1.42108547e-14 30.2933333 134.4 164.48 1.42108547e-14 298.666667 30.2933333 328.96 164.48 194.56 298.666667 328.96 328.96 298.666667 194.56 164.48">
                                </polygon>
                            </g>
                        </g>
                    </svg>
                </button>
            </div>


            {(<button className="subcategory_button" onClick={ChangeInputSubcategory4} ref={subcategory4Standart}><h1>{subcategoria4}</h1></button>)}

            <div ref={editingMenuSubcategory4} className="editing_menu_subcategories">
                <button className="editing_button_subcategories"><h1>{subcategoria4}</h1></button>
                <button className="change_button_subcategories" onClick={EditSubcategory4}>
                    <svg width="60.97px" height="60.97px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd" clip-rule="evenodd" d="M14.2322 5.76777C15.2085 4.79146 16.7915 4.79146 17.7678 5.76777L18.4749 6.47487C19.4512 7.45118 19.4512 9.0341 18.4749 10.0104L10.3431 18.1421L7.10051 18.1421C6.54822 18.1421 6.1005 17.6944 6.10051 17.1421L6.10051 13.8995L14.2322 5.76777ZM16.3536 7.18198L17.0607 7.88909C17.2559 8.08435 17.2559 8.40093 17.0607 8.59619L16 9.65685L14.5858 8.24264L15.6464 7.18198C15.8417 6.98672 16.1583 6.98672 16.3536 7.18198ZM14.5858 11.0711L9.51472 16.1421L8.10051 16.1421L8.10051 14.7279L13.1716 9.65685L14.5858 11.0711Z" fill="#000000"/>
                    </svg>
                </button>
                <button className="change_button_subcategories" onClick={CreateDeleteMenuSubcategory4}>
                    <svg width="86px" height="81.9px" viewBox="0 -0.5 21 21" version="1.1" xmlns="http://www.w3.org/2000/svg">
                        <title>delete [#1487]</title>
                        <desc>Created with Sketch.</desc>
                        <defs>
                        </defs>
                        <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                            <g id="Dribbble-Light-Preview" transform="translate(-179.000000, -360.000000)" fill="#000000">
                                <g id="icons" transform="translate(56.000000, 160.000000)">
                                    <path d="M130.35,216 L132.45,216 L132.45,208 L130.35,208 L130.35,216 Z M134.55,216 L136.65,216 L136.65,208 L134.55,208 L134.55,216 Z M128.25,218 L138.75,218 L138.75,206 L128.25,206 L128.25,218 Z M130.35,204 L136.65,204 L136.65,202 L130.35,202 L130.35,204 Z M138.75,204 L138.75,200 L128.25,200 L128.25,204 L123,204 L123,206 L126.15,206 L126.15,220 L140.85,220 L140.85,206 L144,206 L144,204 L138.75,204 Z" id="delete-[#1487]">
                                    </path>
                                </g>
                            </g>
                        </g>
                    </svg>
                </button>
            </div>
            <div className="delete_menu_container_subcategories" ref={deleteMenuSubcategory4}>
                <button className="delete_button_default_subcategories"><h1>{subcategoria4}</h1></button>
                <button className="change_button_delete_subcategories">
                    <svg width="82.1px" height="57.76px" viewBox="0 0 20 20" version="1.1" xmlns="http://www.w3.org/2000/svg">
                        <g id="layer1">
                            <path d="M 18.837891 3.2832031 L 6.8183594 15.302734 L 1.1621094 9.6464844 L 0.453125 10.353516 L 6.8183594 16.716797 L 19.546875 3.9902344 L 18.837891 3.2832031 z " />
                        </g>
                    </svg>
                </button>
                <button className="change_button_delete_subcategories" onClick={CloseDeleteMenuSubcategory4}>
                    <svg width="55.26px" height="55.26px" viewBox="0 0 512 512" version="1.1" xmlns="http://www.w3.org/2000/svg">
                        <title>cancel</title>
                        <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                            <g id="work-case" fill="#000000" transform="translate(91.520000, 91.520000)">
                                <polygon id="Close" points="328.96 30.2933333 298.666667 1.42108547e-14 164.48 134.4 30.2933333 1.42108547e-14 1.42108547e-14 30.2933333 134.4 164.48 1.42108547e-14 298.666667 30.2933333 328.96 164.48 194.56 298.666667 328.96 328.96 298.666667 194.56 164.48">
                                </polygon>
                            </g>
                        </g>
                    </svg>
                </button>
            </div>
            <div className="subcategories_input_container" ref={editingMenuCreateInputSubcategory4}>
                <input className="input_subcategories"/>
                <button className="change_button_subcategories_create">
                    <svg width="82.1px" height="57.76px" viewBox="0 0 20 20" version="1.1" xmlns="http://www.w3.org/2000/svg">
                        <g id="layer1">
                            <path d="M 18.837891 3.2832031 L 6.8183594 15.302734 L 1.1621094 9.6464844 L 0.453125 10.353516 L 6.8183594 16.716797 L 19.546875 3.9902344 L 18.837891 3.2832031 z " />
                        </g>
                    </svg>
                </button>
                <button className="change_button_subcategories_create" onClick={DefaultSubcategory4}>
                    <svg width="55.26px" height="55.26px" viewBox="0 0 512 512" version="1.1" xmlns="http://www.w3.org/2000/svg">
                        <title>cancel</title>
                        <g id="Page-1" stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                            <g id="work-case" fill="#000000" transform="translate(91.520000, 91.520000)">
                                <polygon id="Close" points="328.96 30.2933333 298.666667 1.42108547e-14 164.48 134.4 30.2933333 1.42108547e-14 1.42108547e-14 30.2933333 134.4 164.48 1.42108547e-14 298.666667 30.2933333 328.96 164.48 194.56 298.666667 328.96 328.96 298.666667 194.56 164.48">
                                </polygon>
                            </g>
                        </g>
                    </svg>
                </button>
            </div>
        </div>
    </>
}

export default Categories