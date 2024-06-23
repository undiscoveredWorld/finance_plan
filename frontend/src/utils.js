import axios from "axios";

export const is_array_equal_array = (array1, array2) => {
    if (array1 === array2) return true
    if (array1 == null || array2 == null) return false
    if (array1.length !== array2.length) return false

    for (let i = 0; i < array1.length; i++) {
        if (array1[i] !== array2[i])
            return false
    }

    return true
}

export const get_and_refresh_rows = (refreshRows) => {
    axios.get("http://5.35.88.46:8080/buys").then((response) => {
        const new_rows = response.data
        refreshRows(new_rows)
    })
}
