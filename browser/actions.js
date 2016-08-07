export const HEAR_FIRE = "HEAR_FIRE"
export const HEAR_JUSTINE = "HEAR_JUSTINE"
export const HEAR_ANTHONY = "HEAR_ANTHONY"
export const NO_FIRE = "NO_FIRE"
export const NO_JUSTINE = "NO_JUSTINE"
export const NO_ANTHONY = "NO_ANTHONY"

export function fireOn() {
    return {
        type: HEAR_FIRE,
        payload: {}
    }
}
export function fireOff() {
    return {
        type: NO_FIRE,
        payload: {}
    }
}
export function anthonyOn() {
    return {
        type: HEAR_ANTHONY,
        payload: {}
    }
}
export function anthonyOff() {
    return {
        type: NO_ANTHONY,
        payload: {}
    }
}
export function justineOn() {
    return {
        type: HEAR_JUSTINE,
        payload: {}
    }
}
export function justineOff() {
    return {
        type: NO_JUSTINE,
        payload: {}
    }
}
