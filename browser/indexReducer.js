import Immutable from 'immutable'
import { HEAR_FIRE, HEAR_JUSTINE, HEAR_ANTHONY, NO_FIRE, NO_JUSTINE, NO_ANTHONY } from './actions.js'

const initialState = Immutable.fromJS({
      isFire: false,
      isJustine: false,
      isAnthony: false
})

function indexReducer(state=initialState, action) {
    switch (action.type) {
        case HEAR_FIRE:
            return state.set('isFire', true)
        case HEAR_JUSTINE:
            return state.set('isJustine', true)
        case HEAR_ANTHONY:
            return state.set('isAnthony', true)
        case NO_FIRE:
            return state.set('isFire', false)
        case NO_JUSTINE:
            return state.set('isJustine', false)
        case NO_ANTHONY:
            return state.set('isAnthony', false)
        default:
            return state
    }
}

export default indexReducer
