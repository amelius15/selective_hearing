import React, { Component, PropTypes } from 'react'

export default class JustineButton extends Component {
    render() {
        return (
            <svg className="justineButton" onClick={ this.props.handleClick }>
                <polygon points="70, 55 70, 145 145, 100" fill="#fff"/>
            </svg>
        )
    }
}

JustineButton.propTypes = {
    handleClick: PropTypes.func.isRequired
}
