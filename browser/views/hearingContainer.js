import Immutable from 'immutable'
import { connect } from 'react-redux'
import Hearing from './hearing'
import { fireOn, fireOff, anthonyOn, anthonyOff, justineOn, justineOff, sendChanges } from '../actions'

function mapStateToProps(state, ownProps) {
    let isFire = state.getIn(['index', 'isFire'])  || false
    let isJustine = state.getIn(['index', 'isJustine']) || false
    let isAnthony = state.getIn(['index', 'isAnthony']) || false

    return {
        isFire: isFire,
        isJustine: isJustine,
        isAnthony: isAnthony
    }
}

function mapDispatchToProps(dispatch, ownProps) {
    return {
        handleFireClick: (e) => {
            e.preventDefault()
            if (ownProps.isFire) {
                dispatch(fireOff())
            }
            else {
                dispatch(fireOn())
            }
            console.log(ownProps)
            console.log(ownProps.isFire)
            console.log(ownProps.isFire ? 'fire' : '')
            dispatch(sendChanges('fire'))
        },
        handleAnthonyClick: (e) => {
            e.preventDefault()
            if (ownProps.isAnthony) {
                dispatch(anthonyOff())
            }
            else {
                dispatch(anthonyOn())
            }
            dispatch(sendChanges('anthony'))
        },
        handleJustineClick: (e) => {
            e.preventDefault()
            if (ownProps.isJustine) {
                dispatch(justineOff())
            }
            else {
                dispatch(justineOn())
            }
            dispatch(sendChanges('justine'))
        }
    }
}

const HearingContainer = connect(mapStateToProps, mapDispatchToProps)(Hearing)

export default HearingContainer
