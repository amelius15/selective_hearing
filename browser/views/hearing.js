import React, { Component, PropTypes } from 'react'
import FireButton from './fireButton'
import AnthonyButton from './anthonyButton'
import JustineButton from './justineButton'

export default class Hearing extends Component {
    render() {
        return (
            <div className='hearing'>
                <h1>selective hearing</h1>
                <h2>for you <em>and</em> your headphones</h2>
                <FireButton onClick={ props.handleFireClick } />
                <AnthonyButton onClick={ props.handleAnthonyClick } />
                <JustineButton onClick={ props.handleJustineClick } />
            </div>
        )
    }
}

Hearing.propTypes = {
    isFire: PropTypes.bool.isRequired,
    isAnthony: PropTypes.bool.isRequired,
    isJustine: PropTypes.bool.isRequired,
    handleFireClick: PropTypes.func.isRequired,
    handleAnthonyClick: PropTypes.func.isRequired,
    handleJustineClick: PropTypes.func.isRequired
}
