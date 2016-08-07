import Immutable from 'immutable'
import indexReducer from './indexReducer'
import routerReducer from './routerReducer'

const initialState = Immutable.Map()
function selectiveHearingApp(state=initialState,  action) {
    return Immutable.Map({
        routing: routerReducer(state.get('routing'), action),
        index: indexReducer(state.get('index'), action)
    })
}

export default selectiveHearingApp
