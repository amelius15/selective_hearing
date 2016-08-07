import React, { Component, PropTypes } from 'react'

export default class AnthonyButton extends Component {
    render() {
        return (
            <svg className="anthonyButton" onClick={ this.props.handleClick }>
                <polygon points="70, 55 70, 145 145, 100" fill="#fff"/>
            </svg>
        )
    }
}

AnthonyButton.propTypes = {
    handleClick: PropTypes.func.isRequired
}
