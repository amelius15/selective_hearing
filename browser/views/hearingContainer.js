import Immutable from 'immutable'
import { connect } from 'react-redux'
import Hearing from './hearing'
import { fireOn, fireOff, anthonyOn, anthonyOff, justineOn, justineOff } from '../actions'

const mapStateToProps = (state) => {
    let isFire = state.getIn(['index', 'isFire'])
    let isJustine = state.getIn(['index', 'isJustine'])
    let isAnthony = state.getIn(['index', 'isAnthony'])
    return {
        isFire: isFire,
        isJustine: isJustine,
        isAnthony: isAnthony
    }
}

const mapDispatchToProps = (dispatch, ownProps) => {
    return {
        handleFireClick: (e) => {
            e.preventDefault()
            if (ownProps.isFire) {
                dispatch(fireOff())
            }
            else {
                dispatch(fireOn())
            }
        },
        handleAnthonyClick: (e) => {
            e.preventDefault()
            if (ownProps.isAnthony) {
                dispatch(anthonyOff())
            }
            else {
                dispatch(anthonyOn())
            }
        },
        handleJustineClick: (e) => {
            e.preventDefault()
            if (ownProps.isJustine) {
                dispatch(justineOff())
            }
            else {
                dispatch(justineOn())
            }
        }
    }
}

const HearingContainer = connect(mapStateToProps, mapDispatchToProps)(Hearing)

export default HearingContainer
